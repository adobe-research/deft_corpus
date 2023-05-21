import csv
import os
from transformers import AutoTokenizer
import torch
from transformers import AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorWithPadding
import numpy as np
from datasets import load_metric

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)


def read_file(directory):
    result = {}
    for file in os.listdir(directory):
        with open(directory + file, encoding="utf-8") as file:
            tsv_file = csv.reader(file, delimiter="\t", quotechar='"')
            for row in tsv_file:
                text = row[0]
                label = int(row[1])
                result[text] = label
    return result


# model_name = "roberta-base"
model_name = "bert-base-uncased"
# model_name = "albert-base-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2).to(device)
path_outputs = "C:/Users/ASUS/Desktop/deft_corpus/data/output/"
all_instances_dic = read_file(path_outputs)
training = {}
validation = {}
test = {}
count = 1
for item in all_instances_dic:
    text = item
    label = all_instances_dic[item]
    if count <= 1680:
        test[text] = label
    elif count <= 2000:
        validation[text] = label
    else:
        training[text] = label
    count += 1

train_encodings = tokenizer(list(training.keys()), truncation=True, padding=True)
val_encodings = tokenizer(list(validation.keys()), truncation=True, padding=True)
test_encodings = tokenizer(list(test.keys()), truncation=True, padding=True)


class TwitterDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


train_dataset = TwitterDataset(train_encodings, list(training.values()))
val_dataset = TwitterDataset(val_encodings, list(validation.values()))
test_dataset = TwitterDataset(test_encodings, list(test.values()))


def compute_metrics(eval_pred):
    load_accuracy = load_metric("accuracy")

    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
    return {"accuracy": accuracy}


model_name = "fine_tuned_classification"
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
training_args = TrainingArguments(
    output_dir=model_name,
    learning_rate=1e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=10,
    save_strategy="no"  # save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()
trainer.save_model()
print(trainer.evaluate())
# Test dataset
trainer.eval_dataset = test_dataset
print(trainer.evaluate())
# or


# trainer.predict(test_dataset)
