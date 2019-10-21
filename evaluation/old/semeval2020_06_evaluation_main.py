"""Evaluation for Semeval 2020 Task 06: DeftEval
How to use:
    1. Adjust settings in the .yaml configuration file
    2. Run this script from the command line

Subtask 01 Input files:
    gold_fname: tab-separated .deft files for Subtask 1 with the following columns (no column headers):
        Sentence    Label
        Label can be HasDef or NoDef
    pred_fname: same format as gold_fname above

Subtask 02 Input files:
    gold_fname: tab-separated .deft files for Subtask 2 with the following columns (no column headers):
        token filename token_start token_end label
    pred_fname: same format as gold_fname above

Subtask 03 Input files:
    gold_fname: tab-separated .deft files for Subtask 3 with the following columns (no column headers):
        token filename token_start token_end label tag_id relation_root relation_name
    pred_fname: same format as gold_fname above

Notes:
    1. pred_fname must have the same columns as gold_fname in the same order
    2. all columns in pred_fname must have the same data as in gold_fname, except for the columns being predicted
        - i.e. label for Subtask 2 and relation_root and relation_name for Subtask 3
    3. pred_fname may not contain any relations that did not appear in the training data
"""

from pathlib import Path
from yaml import safe_load

from semeval2020_0601_eval import task_1_eval_main
from semeval2020_0602_eval import task_2_eval_main
from semeval2020_0603_eval import task_3_eval_main

CFG_FNAME = Path("./configs/eval_test.yaml")

def main(cfg):
    """Run the evaluation script(s)
    Inputs:
        cfg: configuration dictionary loaded from yaml
    """

    eval_task_1 = cfg['task_1']['do_eval']
    eval_task_2 = cfg['task_2']['do_eval']
    eval_task_3 = cfg['task_3']['do_eval']

    if eval_task_1: 
        task_1_gold_fname = Path(cfg['task_1']['gold_fname'])
        task_1_pred_fname = Path(cfg['task_1']['pred_fname'])
        task_1_eval_labels = cfg['task_1']['eval_labels']
        task_1_report = task_1_eval_main(task_1_gold_fname, task_1_pred_fname, task_1_eval_labels)
        print(task_1_report)
        print()

    if eval_task_2:
        task_2_gold_fname = Path(cfg['task_2']['gold_fname'])
        task_2_pred_fname = Path(cfg['task_2']['pred_fname'])
        task_2_eval_labels = cfg['task_2']['eval_labels']
        task_2_report = task_2_eval_main(task_2_gold_fname, task_2_pred_fname, task_2_eval_labels)
        print(task_2_report)
        print()

    if eval_task_3:
        task_3_gold_fname = Path(cfg['task_3']['gold_fname'])
        task_3_pred_fname = Path(cfg['task_3']['pred_fname'])
        task_3_eval_labels = cfg['task_3']['eval_labels']
        task_3_report = task_3_eval_main(task_3_gold_fname, task_3_pred_fname, task_3_eval_labels)
        print(task_3_report)
        print()

if __name__ == "__main__":
    with CFG_FNAME.open() as source:
        cfg = safe_load(source)
        main(cfg)

