from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Modèle
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# "Base de données" temporaire
items = []

@app.get("/")
def root():
    return {"message": "Bienvenue sur mon API"}

@app.get("/items", response_model=List[Item])
def get_items():
    return items

@app.post("/items", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

@app.get("/items/{index}")
def get_item(index: int):
    if index >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[index]