from sentence_transformers import SentenceTransformer


class SentenceEmbedder:
    """
    Wrapper around the SentenceTransformer model.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def encode(self, text, convert_to_tensor=True):
        return self.model.encode(
            text,
            convert_to_tensor=convert_to_tensor,
        )