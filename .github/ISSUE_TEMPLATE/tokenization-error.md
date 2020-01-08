---
name: Tokenization Error
about: Use this for reporting suspected tokenization errors
title: "[TOKENIZATION]"
labels: tokenization
assignees: sashaspala

---

#### Filepath ####
Please provide the file and parent folder (dev/train/test) where you found the error.
i.e., `dev/t1_biology_0_0.deft`
#### Content ####
Please provide a copy of the exact sentence(s) of the error in .deft format. Please also provide the line numbers where this sentence occurs.
i.e.,
```
It	 data/source_txt/t1_biology_jlee_0.txt	 3	 5	 O	 -1	 -1	 0
becomes	 data/source_txt/t1_biology_jlee_0.txt	 6	 13	 O	 -1	 -1	 0
clear	 data/source_txt/t1_biology_jlee_0.txt	 14	 19	 O	 -1	 -1	 0
from	 data/source_txt/t1_biology_jlee_0.txt	 20	 24	 O	 -1	 -1	 0
this	 data/source_txt/t1_biology_jlee_0.txt	 25	 29	 O	 -1	 -1	 0
definition	 data/source_txt/t1_biology_jlee_0.txt	 30	 40	 O	 -1	 -1	 0
that	 data/source_txt/t1_biology_jlee_0.txt	 41	 45	 O	 -1	 -1	 0
the	 data/source_txt/t1_biology_jlee_0.txt	 46	 49	 O	 -1	 -1	 0
application	 data/source_txt/t1_biology_jlee_0.txt	 50	 61	 O	 -1	 -1	 0
of	 data/source_txt/t1_biology_jlee_0.txt	 62	 64	 O	 -1	 -1	 0
the	 data/source_txt/t1_biology_jlee_0.txt	 65	 68	 O	 -1	 -1	 0
scientific	 data/source_txt/t1_biology_jlee_0.txt	 69	 79	 O	 -1	 -1	 0
method	 data/source_txt/t1_biology_jlee_0.txt	 80	 86	 O	 -1	 -1	 0
plays	 data/source_txt/t1_biology_jlee_0.txt	 87	 92	 O	 -1	 -1	 0
a	 data/source_txt/t1_biology_jlee_0.txt	 93	 94	 O	 -1	 -1	 0
major	 data/source_txt/t1_biology_jlee_0.txt	 95	 100	 O	 -1	 -1	 0
rolein	 data/source_txt/t1_biology_jlee_0.txt	 101	 108	 O	 -1	 -1	 0
science	 data/source_txt/t1_biology_jlee_0.txt	 109	 116	 O	 -1	 -1	 0
.	 data/source_txt/t1_biology_jlee_0.txt	 116	 117	 O	 -1	 -1	 0
```
Lines 4-21. Error in line 19.

#### Additional Information ####
Any other information you think we would find helpful should go here. If you have found this error multiple times, please provide the additional locations. 

Note that some tokenization eccentricities may not in fact be errors (e.g. contractions on a separate line). We will try to review all tokenization error reports and respond within 3 business days.
