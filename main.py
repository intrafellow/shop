import uvicorn
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI
from items_view import router as items_router

app = FastAPI()
app.include_router(items_router)


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


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)