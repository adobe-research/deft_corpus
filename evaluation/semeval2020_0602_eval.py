"""Evaluation script for Semeval 2020 Task 2: DeftEval Sequence Labeling
How to use:
    Used by semeval2020_06_evaluation_main.py, which is the main entry point into the evaluation scripts

Input files:
    gold_fname: tab-separated .deft files for Subtask 2 with the following columns (no column headers):
        token filename token_start token_end label
    pred_fname: same format as gold_fname above

Notes:
    1. pred_fname must have the same columns as gold_fname in the same order
    2. pred_fname may not contain any labels that did not appear in the training data
"""
import csv
from sklearn.metrics import classification_report


def get_token(row):
    """Get the token from the row
    Inputs:
        row: list of strings
    Returns:
        token: string
    """
    return row[0]


def get_label(row):
    """Get the label from the row
    Inputs:
        row: list of strings
    Returns:
        label: string
    """
    return row[-1]


def validate_length(gold_rows, pred_rows):
    """Check that gold and pred files have same number of rows
    Inputs:
        gold_rows: list of lists of strings
        pred_rows: list of lists of strings
    """
    if len(pred_rows) != len(gold_rows):
        raise ValueError("Row length mismatch: Pred {} Gold {}".format(len(pred_rows), len(gold_rows)))


def validate_columns(gold_rows, pred_rows):
    """Check correct number of (and correct data in) columns
     Inputs:
        gold_rows: list of lists of strings
        pred_rows: list of lists of strings
    """
    pass


def validate_tokens(gold_rows, pred_rows):
    """Check that gold and pred files have same tokens in each row
     Inputs:
        gold_rows: list of lists of strings
        pred_rows: list of lists of strings
    """
    for row_index in range(len(pred_rows)):
        gold_token = get_token(gold_rows[row_index])
        pred_token = get_token(pred_rows[row_index])
        if pred_token != gold_token:
            raise ValueError("Token mismatch row {}: Pred {} Gold {}".format(row_index, pred_token, gold_token))


def validate_labels(gold_rows, pred_rows):
    """Check that pred file doesn't have any unknown labels
      Inputs:
        gold_rows: list of lists of strings
        pred_rows: list of lists of strings
    """
    unknown_labels = list()  # [(row, label)]
    gold_labels = set([get_label(row) for row in gold_rows])
    for row_index in range(len(pred_rows)):
        pred_label = get_label(pred_rows[row_index])
        if pred_label not in gold_labels:
            unknown_labels.append((row_index, pred_label))

    if unknown_labels:
        raise ValueError("Encountered unknown label in the following rows {}".format(unknown_labels))


def validate_data(gold_rows, pred_rows):
    """Make sure the data is OK
    Inputs:
        gold_rows: list of lists of strings
        pred_rows: list of lists of strings
    """
    validate_length(gold_rows, pred_rows)
    validate_columns(gold_rows, pred_rows)
    validate_tokens(gold_rows, pred_rows)
    validate_labels(gold_rows, pred_rows)


def get_gold_and_pred_labels(gold_fname, pred_fname):
    """Get the labels for evaluation
    Inputs:
        gold_fname: path to .deft file
        pred_fname: path to .deft file
    Returns:
        y_gold: list of labels (strings)
        y_pred: list of labels (strings)
    """
    with gold_fname.open() as gold_source:
        gold_reader = csv.reader(gold_source, delimiter="\t")
        gold_rows = [row for row in gold_reader if row]

    with pred_fname.open() as pred_source:
        pred_reader = csv.reader(pred_source, delimiter="\t")
        pred_rows = [row for row in pred_reader if row]

    validate_data(gold_rows, pred_rows)
    y_gold = [get_label(row) for row in gold_rows]
    y_pred = [get_label(row) for row in pred_rows]
    return y_gold, y_pred


def evaluate(y_gold, y_pred, eval_labels):
    """Get the scores
    Inputs:
        y_gold: list of labels (strings)
        y_pred: list of labels (strings)
        eval_labels: set of labels to evaluate on (e.g. excluding 'O', etc.)
    Returns:
        sklearn classification report (string)
    """
    return classification_report(y_gold, y_pred, target_names=eval_labels)


def task_2_eval_main(gold_fname, pred_fname, eval_labels):
    """Evaluate the data
    Inputs:
        gold_fname: path of .deft file
        pred_fname: path of .deft file
        eval_labels: set of labels to evaluate on
    Returns:
        sklearn classification report
    """
    y_gold, y_pred = get_gold_and_pred_labels(gold_fname, pred_fname)
    report = evaluate(y_gold, y_pred, eval_labels)
    return report
