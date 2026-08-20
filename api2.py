from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Beispiel API mit Response Modellen",
    description="Beispiel API mit Response Modellen",
    version="1.0.0"
)


class Item(BaseModel):
    item_id : int
    name : str
    query : str

class Product(BaseModel):
    id: int
    name: str
    price: float

class Category(BaseModel):
    id: int
    name: str
    products: List[Product]

@app.get("/")
def root():
    return {"message": "it works!"}


# Endpunkt mit Einem Response Model
@app.get(
    "/items/{item_id}",
    response_model=Item
)
def read_item(item_id: int, q: str = None):
    # code der den datensatz aus der DB holt
    data = {
        "item_id": item_id,
        "name" :"Ein Beispiel",
        "query": q
    }
    return data


# Endpunkt mit verschachtelten Daten
@app.get("/categories/{cat_id}", response_model=Category)
def get_category(cat_id: int):
    # Fake-Daten (statt DB)
    return {
        "id": cat_id,
        "products": [
            {"id": 1, "name": "Laptop" },
            {"id": 2, "name": "Maus" }
        ]
    }


# Endpunkt mit eigenem Fehlercode
@app.get("/exampleerror")
def exampleerror():

    if 2 != 3 :
        raise HTTPException(
            status_code=404,
            detail="Meine Eigene Fehlermeldung"
        )





