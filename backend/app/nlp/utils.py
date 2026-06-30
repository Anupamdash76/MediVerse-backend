import joblib

from app.config.paths import ARTIFACT_DIR


def save_artifact(obj, filename):

    joblib.dump(
        obj,
        ARTIFACT_DIR / filename,
    )


def load_artifact(filename):

    return joblib.load(
        ARTIFACT_DIR / filename,
    )