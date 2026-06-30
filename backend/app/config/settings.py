"""
Application settings for MediVerse.

Contains:
- NLP configuration
- Database configuration
- Authentication configuration
"""

import os

from dotenv import load_dotenv

load_dotenv()


# =====================================================
# NLP Configuration
# =====================================================

# Number of semantic matches to retrieve
TOP_K = 3

# Minimum cosine similarity score
# required for a symptom to be considered a match.
SIMILARITY_THRESHOLD = 0.75


# =====================================================
# Database Configuration
# =====================================================

MONGODB_URL = os.getenv("MONGODB_URL")

DATABASE_NAME = os.getenv("DATABASE_NAME")


# =====================================================
# JWT Configuration
# =====================================================

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        60,
    )
)