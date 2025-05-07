from sentence_transformers import SentenceTransformer, util

class QAEngine:
    def __init__(self, text):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sentences = [s.strip() for s in text.split('\n') if s.strip()]
        self.embeddings = self.model.encode(self.sentences, convert_to_tensor=True)
    
    def ask(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.cos_sim(query_embedding, self.embeddings)[0]
        best_match_idx = scores.argmax().item()
        return self.sentences[best_match_idx]