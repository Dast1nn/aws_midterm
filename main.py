# main.py
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World! Dastan "}


@app.get("/health")
def health_check():
    return {"status": "OK"}
