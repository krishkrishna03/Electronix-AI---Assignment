import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import argparse
import numpy as np
import random
import os

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

parser = argparse.ArgumentParser()
parser.add_argument('-data', type=str, required=True)
parser.add_argument('-epochs', type=int, default=3)
parser.add_argument('-lr', type=float, default=3e-5)
args = parser.parse_args()

set_seed()

dataset = load_dataset("json", data_files=args.data, split="train")

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
def preprocess(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=128)
dataset = dataset.map(preprocess, batched=True)
label2id = {"negative":0, "positive":1}
dataset = dataset.map(lambda e: {"label": label2id[e["label"]]})

model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)

training_args = TrainingArguments(
    output_dir="./model",
    num_train_epochs=args.epochs,
    learning_rate=args.lr,
    per_device_train_batch_size=8,
    save_total_limit=1,
    load_best_model_at_end=True,
    logging_dir='./logs',
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

trainer.train()
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")
