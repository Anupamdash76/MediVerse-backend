import torch
from sentence_transformers import util

from app.config.settings import (
    TOP_K,
    SIMILARITY_THRESHOLD,
)


class SimilarityEngine:
    """
    Computes semantic similarity between
    the user's symptom and all known symptoms.
    """

    def __init__(self, symptom_embeddings):

        self.symptom_embeddings = symptom_embeddings

    def find_matches(
        self,
        query_embedding,
        top_k=TOP_K,
        threshold=SIMILARITY_THRESHOLD,
    ):
        """
        Returns the best semantic matches.

        Parameters
        ----------
        query_embedding
            Sentence embedding of the user's symptom.

        top_k
            Maximum number of matches.

        threshold
            Minimum cosine similarity.

        Returns
        -------
        list[dict]

        [
            {
                "index": 25,
                "score": 0.96,
            },
            ...
        ]
        """

        cosine_scores = util.pytorch_cos_sim(
            query_embedding,
            self.symptom_embeddings,
        )[0]

        scores, indices = torch.topk(
            cosine_scores,
            k=min(top_k, len(cosine_scores)),
        )

        matches = []

        for score, index in zip(scores, indices):

            score = float(score)

            if score < threshold:
                continue

            matches.append(
                {
                    "index": int(index),
                    "score": score,
                }
            )

        return matches

    def find_best_match(
        self,
        query_embedding,
        threshold=SIMILARITY_THRESHOLD,
    ):
        """
        Returns only the highest-confidence match.
        """

        matches = self.find_matches(
            query_embedding=query_embedding,
            top_k=1,
            threshold=threshold,
        )

        if not matches:
            return None

        return matches[0]