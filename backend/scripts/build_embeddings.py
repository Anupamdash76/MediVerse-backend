import torch

from app.config.paths import MODEL_DIR
from app.nlp.embeddings import EmbeddingGenerator
from app.nlp.utils import load_artifact


def main():

    feature_names = load_artifact(
        "feature_names.pkl"
    )

    print(f"Loaded {len(feature_names)} features.")

    generator = EmbeddingGenerator()

    embeddings = generator.build(
        feature_names
    )

    torch.save(
        embeddings,
        MODEL_DIR / "symptom_embeddings.pt",
    )

    print("Embeddings generated successfully!")


if __name__ == "__main__":
    main()