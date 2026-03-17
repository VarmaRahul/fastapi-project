from fastapi import FastAPI, Depends
from typing import Annotated
from test import QueryParams

app = FastAPI()

@app.get("/")
def root(query: Annotated[QueryParams, Depends()]):
    return {"Message":"Hello FastAPI", "params": query}


@app.post("/todo")
def create_todo(item: dict) -> dict:
    return {"Message":"Added todo item", "Item": item}

