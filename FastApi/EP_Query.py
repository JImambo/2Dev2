""" ENDPOINT AVEC QUERY PARAMETER """
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/items/")
async def get_items(q: str, limit: int = 10):
    return {
        "query": q,
        "limit": limit
    }
