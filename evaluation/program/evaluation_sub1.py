import sys
from pathlib import Path
import csv
import os
from sklearn.metrics import classification_report
import warnings

"""Evaluation script for Semeval 2020 Task 06 Subtask 01: DeftEval Sentence Classification
How to use:
    Used by semeval2020_06_evaluation_main.py, which is the main entry point into the evaluation scripts

Input files:
    gold_fname: tab-separated .deft files for Subtask 1 with the following columns (no column headers):
        Sentence    Label
        Label can be HasDef or NoDef
    pred_fname: same format as gold_fname above
"""

def get_sent(row):
    """Get the sentence from the row
    Inputs:
        row: list of strings
    Returns:
        sentence: string
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


def validate_sents(gold_rows, pred_rows):
    """Check that gold and pred files have same sentences in each row
     Inputs:
        gold_rows: list of lists of strings
        pred_rows: list of lists of strings
    """
    for row_index in range(len(pred_rows)):
        gold_sent = get_sent(gold_rows[row_index])
        pred_sent = get_sent(pred_rows[row_index])
        if pred_sent != gold_sent:
            raise ValueError("Sentence mismatch row {}: Pred {} Gold {}".format(row_index, pred_sent, gold_sent))


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
    validate_sents(gold_rows, pred_rows)
    # validate_labels(gold_rows, pred_rows) #Todo: validate these against true labels we expect, not just what's in the gold file.


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
    return classification_report(y_gold, y_pred, labels=eval_labels, output_dict=True)

def write_to_scores(report, output_fname):
    """ Prints scores to scores.txt
    Inputs:
        report: classification_report generated from evaluate()
    Returns:
        None
    """
    with open(output_fname, 'a+') as scores_file:

        scores_file.write('subtask_1_accuracy: ' + str(report['1']['f1-score']) + '\n')


def task_1_eval_main(ref_path, res_path, output_dir, eval_labels):
    """Evaluate the data
    Inputs:
        gold_fname: path of .deft file
        pred_fname: path of .deft file
        eval_labels: set of labels to evaluate on
    Returns:
        sklearn classification report
    """

    y_gold = []
    y_pred = []

    reference_files = []
    results_files = []

    for child in res_path.iterdir():
        if child.name.startswith('task_1'):
            results_files.append(child.name)
            if not os.path.exists(ref_path.joinpath(child.name)):
                message = "Expected submission file '{0}', found files {1}"
                sys.exit(message.format(child, os.listdir(child.parents[0])))

            temp_y_gold, temp_y_pred = get_gold_and_pred_labels(ref_path.joinpath(child.name), child)
            y_gold.extend(temp_y_gold)
            y_pred.extend(temp_y_pred)

    if len(results_files) == 0:
        message = "No subtask 1 files to evaluate."
        warnings.warn(message)
        return None

    for child in ref_path.iterdir():
        if child.name.startswith('task_1'):
            reference_files.append(child.name)

    missing = [file for file in reference_files if file not in results_files]
    if len(missing) > 0:
        message = "Missing evaluation files {0}"
        sys.exit(message.format(str(missing)))

    report = evaluate(y_gold, y_pred, eval_labels)
    write_to_scores(report, Path(output_dir).joinpath('scores.txt'))
    return report

