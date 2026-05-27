from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

@app.get("/") #This is called a path operation similar to endpoints in flask
async def print_hello():
    return {"message" : "Hello world"}

@app.get("/get_item/{item_id}") #Here item_id is a path parameter and q is query parameter
async def get_item(item_id : int, q : str | None = None):
    return {"item_id" : item_id, "q" : q}

class Item(BaseModel):
    name : str
    price : int
    is_offer : bool | None = None

@app.put("/update_item/{item_id}")
async def update_item(item_id : int, item : Item):
    item.name = "Car"
    item.price = 5000
    item.is_offer = True
    return {"item_id" : item_id, "item_name" : item.name, "price" : item.price,
             "is_offer" : item.is_offer}

class ColorChoices(str, Enum): #Enum is used to get predefined choices in path parameter
    red = "Red"
    blue = "Blue"
    green = "Green"

@app.post("/color_choices/{color}")
async def color_choices(color : ColorChoices):
    if color.value == "Red":
        return {"message" : "Car is colored red"}
    elif color is ColorChoices.blue:
        return {"message" : "Car is colored blue"}
    elif color == ColorChoices.green.value:
        return {"message" : "Car is colored green"}
    
#file_path : path is used to determine that path parameter must match a file path    
@app.get("/files/{file_path : path}")
async def file_path_getter(file_path : str):
    return {"file_path" : file_path}
    


 