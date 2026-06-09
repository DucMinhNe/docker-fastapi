"""minhle202/fastapi — Python 3.12 + FastAPI + Uvicorn REST API starter.

Part of the branded Docker Hub starter-image family by Lê Đức Minh.
"""
import time

from fastapi import FastAPI

# Captured once at import so /health can report process uptime.
_START_TIME = time.monotonic()

APP_NAME = "docker-fastapi"
APP_VERSION = "1.0.0"

app = FastAPI(title=APP_NAME, version=APP_VERSION)


@app.get("/")
def root():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "endpoints": ["/", "/health", "/api/hello"],
    }


@app.get("/health")
def health():
    return {"status": "ok", "uptime": time.monotonic() - _START_TIME}


@app.get("/api/hello")
def hello(name: str = "world"):
    return {"message": f"Hello, {name}!"}
