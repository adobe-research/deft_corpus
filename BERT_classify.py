import torch
from transformers import pipeline

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)


model_name = "fine_tuned_model"
classifier = pipeline("text-classification", model=model_name)
text = "text goes here."
result = classifier(text)[0]
label = result['label']
if label == "LABEL_1":
    print("it is a sentence with definition")
else:
    print("not a definition")
