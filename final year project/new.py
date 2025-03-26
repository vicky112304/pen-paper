from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
sentence1 = "Achieving success requires perseverance and the ability to adapt"
sentence2 = "Requires perseverance and the ability to adapt"
embedding1 = model.encode([sentence1])
embedding2 = model.encode([sentence2])
similarity = cosine_similarity(embedding1, embedding2)
print(f"Similarity: {similarity[0][0]*100}%")