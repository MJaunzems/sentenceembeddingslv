import numpy as np
import fasttext

file_path = "Final_Sent_50_2.txt"
output_path = "FastText_Final_Sent_50_2.txt"
model = fasttext.load_model("cc.lv.300.bin")
with open(file_path, "r", encoding="utf-8") as file:
    sentences = file.readlines()
sentences = [sentence.strip() for sentence in sentences]
embeddings = np.array([model.get_sentence_vector(sentence) for sentence in sentences])
m=0
with open(output_path, "w") as file:
    for i in range(len(sentences)):
        embedding_str = " ".join([str(x) for x in embeddings[i]])
        file.write(embedding_str + "\n")
        m+=1
        print(m)