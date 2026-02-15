from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load SBERT model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(text1, text2):
    """
    Returns semantic similarity score between two texts (0 to 1)
    """
    emb1 = model.encode([text1])
    emb2 = model.encode([text2])
    return cosine_similarity(emb1, emb2)[0][0]
