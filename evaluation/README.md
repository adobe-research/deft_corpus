# Evaluation scripts for SemEval 2020 Task 06: DeftEval

## Scripts

* `semeval2020_0601_eval.py` evaluation script for Subtask 01 (sentence classification)
* `semeval2020_0602_eval.py` evaluation script for Subtask 02 (sequence labeling)
* `semeval2020_0603_eval.py` evaluation script for Subtask 03 (relation extraction)
* `semeval2020_06_evaluation_main.py` entry point for running one or move of the above evaluation scripts

## Directories

* `configs` yaml file(s) with configurations (which evaluations to run, data files, etc.)
* `data` gold and predicted data in .deft format (just samples for now)

## How to use

Follow the instructions in the comments of `semeval2020_06_evaluation_main.py`

## Evaluation Criteria

1. Subtask 1: Sentence Classification 

We will report P/R/F1 for the positive and negative classes. The official score will be based on the F1 for the positive class.

2. Subtask 2: Sequence labeling

We will report P/R/F1 for each evaluated class, as well as macro- and micro-averaged F1 for the evaluated classes. The official score will be based on  the macro-averaged F1 of the evaluated classes. Evaluated classes are Term, Alias-Term, Referential-Term, Definition, Referential-Definition, and Qualifier.

3. Subtask 3: Relation extraction

We will report P/R/F1 for each evaluated relation, as well as macro- and micro-averaged F1 for the evaluated relations. The official score will be based on  the macro-averaged F1 of the evaluated relations. The evaluated relations are Direct-defines, Indirect-defines, Refers-to, AKA, and Qualifies.
