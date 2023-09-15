from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from laserembeddings import Laser
laser = Laser()
input_file = "Final_Sent_50_2.txt"
with open(input_file, "r", encoding="utf-8") as f:
    sentences = [line.strip() for line in f.readlines()]
embeddings = laser.embed_sentences(sentences, lang="lv")
output_file = "LASER_Final_Sent_50_2.npy"
np.save(output_file, embeddings)
