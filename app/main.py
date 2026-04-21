from fastapi import FastAPI
import os

app = FastAPI()

APP_ENV = os.getenv("APP_ENV", "dev")
APP_VERSION = os.getenv("APP_VERSION", "unknown")

@app.get("/")
def home():
    return {
        "message": f"Application is running in {APP_ENV}",
        "version": APP_VERSION
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "environment": APP_ENV,
        "version": APP_VERSION
    }