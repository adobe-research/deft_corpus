# Welcome to the DEFT corpus!
Welcome to the largest expertly annotated corpus for complex definition extraction in free text. Pardon our dust - this data is associated with [SemEval 2020 Task 6](https://competitions.codalab.org/competitions/20900) (DeftEval) and we are releasing the full dataset on the SemEval conference schedule. Dev and trial data are available now, and training data will become available on 4 Sept 2019. Test data will be released after the completion of the SemEval evaluation period on 2 Feb 2020. You can source the complete text from the corresponding textbooks at <https://cnx.org>.

In the meantime, please use the current version of the corpus.
The most recent version of the corpus was updated on **28 AUG 2019**.

For more information regarding the annotation, schema, or general characteristics of the coprus, please see our paper [here](https://sigann.github.io/LAW-XIII-2019/pdf/W19-4015.pdf).
  
# Data Format
We are currently releasing data in conll 2003-like format with the formatting as follows:

TOKEN TXT_SOURCE_FILE START_CHAR END_CHAR TAG TAG_ID ROOT_ID RELATION

Character indices are derived from brat standoff format. Tags follow a BIO format with the tag schema outlined in the paper.

# Licensing Information
The entire dataset of textbook sentences with annotations is available for use under the [CC BYNA-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) license. Contact the authors for information on commercial use.

