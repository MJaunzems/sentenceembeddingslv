import numpy as np
import faiss

with open("mBERT_Simple_1.npy", "rb") as f:
    xb = np.load(f)
with open("mBERT_Simple_2.npy", "rb") as f:
    xq = np.load(f)
n1, d = xb.shape
n2, d = xb.shape
M = 64
ef_search = 32
ef_construction = 64
index = faiss.IndexHNSWFlat(d, M)
index.hnsw.efConstruction = ef_construction
index.hnsw.efSearch = ef_search
index.add(xb)
k = 1
tp = 0
fp = 0
fn = 0
mrr_sum = 0
for i in range(n1):
    found_relevant_result = False
    query_embedding = xq[i]
    D, I = index.search(query_embedding.reshape(1, -1), k)
    rank = 0
    for j in range(k):
        neighbor_index = I[0][j]
        if neighbor_index == i:
            tp+=1
            found_relevant_result = True
        else:
            fp+=1
    if not found_relevant_result:
        fn += 1
    m, n = index.search(query_embedding.reshape(1, -1), n2)
    for j in range(n2):
        neighbor_index = n[0][j]
        if neighbor_index == i:
            rank = j + 1
            mrr_sum += (1/rank)
            break
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * precision * recall / (precision + recall)
mrr = mrr_sum/n1
print("Precision: {:.4f}".format(precision))
print("Recall: {:.4f}".format(recall))
print("F1-score: {:.4f}".format(f1_score))
print("MRR:  {:.4f}".format(mrr))
