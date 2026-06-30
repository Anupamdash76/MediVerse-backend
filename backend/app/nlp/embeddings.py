import torch

from app.nlp.embedder import SentenceEmbedder


class EmbeddingGenerator:

    def __init__(self):
        self.embedder = SentenceEmbedder()

    def build(self, symptoms):

        embeddings = self.embedder.encode(symptoms)

        return embeddings

    def save(self, embeddings, path):

        torch.save(
            embeddings,
            path,
        )