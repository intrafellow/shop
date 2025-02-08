import uvicorn
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get("/")
def hello_index():
    return {
        "message": "Hello, world!"
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello, {name}"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }


@app.post("/users")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }


@app.get("/items/")
def items_list():
    return [
        "Item1",
        "Item2",
        "Item3"
    ]


@app.get("/items/latest/")
def get_latest_item():
    return {"id" : "0", "name": "latest"}


@app.get("/items/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {
        'Item': {
            "id" : item_id
        }
    },


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)