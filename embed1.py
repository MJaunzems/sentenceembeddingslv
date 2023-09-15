from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("WENGSYX/Multilingual_SimCSE")
model = AutoModel.from_pretrained("WENGSYX/Multilingual_SimCSE")
def generate_embeddings(sentences, batch_size=32):
    embeddings_list = []
    for i in range(0, len(sentences), batch_size):
        batch_sentences = sentences[i:i+batch_size]
        encoded_input = tokenizer(batch_sentences, padding=True, truncation=True, max_length=128, return_tensors='pt')
        with torch.no_grad():
            model_output = model(**encoded_input)
            embeddings = model_output[0][:, 0, :]
        embeddings_list.append(embeddings)
        print(i)
    embeddings = torch.cat(embeddings_list, dim=0)
    return embeddings.numpy()
input_file = "Simple_2.txt"
with open(input_file, "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f.readlines()]
embeddings = generate_embeddings(sentences, batch_size=32)
output_file = "mSimCSE_Simple_2.npy"
np.save(output_file, embeddings)
