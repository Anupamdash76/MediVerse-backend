from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.prediction import router as prediction_router
from app.auth.router import router as auth_router
from app.profile.router import router as profile_router
from app.history.router import router as history_router

app = FastAPI(
    title="MediVerse API",
    description="AI-powered disease prediction using NLP and XGBoost.",
    version="1.0.0",
)


# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# API Routers
# -----------------------------
app.include_router(
    prediction_router,
    prefix="/api/v1",
)
app.include_router(
    profile_router,
    prefix="/api/v1",
)

app.include_router(
    auth_router,
    prefix="/api/v1",
)

app.include_router(
    history_router,
    prefix="/api/v1",
)

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
async def root():

    return {
        "project": "MediVerse",
        "version": "1.0.0",
        "status": "Running",
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
async def health():

    return {
        "status": "Healthy",
    }