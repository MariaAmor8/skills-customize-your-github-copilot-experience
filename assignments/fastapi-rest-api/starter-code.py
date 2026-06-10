from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    price: float


items = [
    {"id": 1, "name": "Notebook", "description": "A lined notebook", "price": 3.5},
    {"id": 2, "name": "Pen", "description": "Blue ink pen", "price": 1.25},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment"}


@app.get("/items")
def list_items():
    # Return all items in memory
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    # Find and return a single item by id
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    # Add a new item to the in-memory list
    new_item = {"id": len(items) + 1, **item.model_dump()}
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    # Update an existing item
    for index, current_item in enumerate(items):
        if current_item["id"] == item_id:
            updated_item = {"id": item_id, **item.model_dump()}
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Delete an item by id
    for index, current_item in enumerate(items):
        if current_item["id"] == item_id:
            removed_item = items.pop(index)
            return {"deleted": removed_item}
    raise HTTPException(status_code=404, detail="Item not found")


# Students can run this file with:
# uvicorn starter-code:app --reload