from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

from transformers import AutoTokenizer, AutoModel
import torch

model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


words = ["māja", "dzīvoklis", "jūra"]

def get_embeddings(words):
    embeddings = []
    for word in words:
        inputs = tokenizer(word, return_tensors="pt")
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())
    return embeddings

embeddings = get_embeddings(words)

similarities = cosine_similarity(embeddings)

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        print(f"Similarity between '{words[i]}' and '{words[j]}': {similarities[i][j]:.4f}")
