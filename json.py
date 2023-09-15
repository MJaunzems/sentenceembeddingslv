import json
import os

jsonl_path = "path/to/your/file.jsonl"
sentence_1_path = "path/to/output/sentence_1.txt"
sentence_2_path = "path/to/output/sentence_2.txt"
with open(jsonl_path, "r") as f:
    for line in f:
        json_obj = json.loads(line)
        sentence_1 = json_obj["set"][0]
        sentence_2 = json_obj["set"][1]
        with open(sentence_1_path, "a") as f_sentence_1:
            f_sentence_1.write(sentence_1 + "\n")
        with open(sentence_2_path, "a") as f_sentence_2:
            f_sentence_2.write(sentence_2 + "\n")
