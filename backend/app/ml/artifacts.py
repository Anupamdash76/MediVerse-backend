import joblib

from app.config.paths import MODEL_DIR


def save_artifact(obj, filename: str):
    """
    Save any Python object as a Joblib artifact.
    """

    joblib.dump(
        obj,
        MODEL_DIR / filename,
    )