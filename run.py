from fastapi import FastAPI
import os

app = FastAPI()
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
