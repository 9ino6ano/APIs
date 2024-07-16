from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None


inventory = {
    1: {
        "name": "Milk",
        "price": "3.99",
        "brand": "Regular"
    }
}

"""
GET,POST,PUT,DELETE
"""
@app.get("/")
def home():
    return {"Data": "Tested"}

@app.get("/about")
def about():
    return {"Data": "About"}

"""
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str):
    return inventory[item_id]
"""
"""
adding more constraints to path parameters
> using gt,lt,ge
"""
"""
Using @Path Parameters
127.0.0.1/get-item/1
"""
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you want to view ", gt=0)):
    return inventory[item_id]


"""
Using @Query Parameters
127.0.0.1/get-by-name?name=Milk
http://127.0.0.1:8000/get-by-name?test=1&name=Milk
combining path and query parameters
http://127.0.0.1:8000/get-by-name/1?test=1&name=Milk



@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not Found"}
    raise HTTPException(status_code=404, detail="Item name not found.")

"""


@app.get("/get-by-name/{item_id}")
def get_item(name: str = Query(None, title="Name", description="Name of Item",max_length=10, min_length=2)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not Found"}
    raise HTTPException(status_code=404, detail="Item name not found.")

"""
using the request body method
"""


@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {'Error': "ID already exits."}
        raise HTTPException(status_code=404, detail="Item name not found.")
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]


"""
The update method
"""
@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id in inventory:
        return {'Error': "ID doesn't exits."}
    if item_id != None:
        inventory[item_id].name = item.name
    if item_id != None:
        inventory[item_id].price = item.price
    if item_id != None:
        inventory[item_id].brand = item.brand

    return inventory[item_id]

"""
The delete method
"""

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description = "The ID of the item you want to delete")):
    if item_id not in inventory:
        return {"Error": "ID does not exist"}

    del inventory[item_id]
    return {"Success": "Item Deleted!!"}