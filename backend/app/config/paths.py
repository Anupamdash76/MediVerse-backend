from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]

# Directories
APP_DIR = BASE_DIR / "app"
DATASET_DIR = BASE_DIR / "dataset"

MODEL_DIR = BASE_DIR / "models"
ARTIFACT_DIR = BASE_DIR / "artifacts"

SCRIPT_DIR = BASE_DIR / "scripts"

MODEL_DIR.mkdir(exist_ok=True)
ARTIFACT_DIR.mkdir(exist_ok=True)