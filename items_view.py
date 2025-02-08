from typing import Annotated
from fastapi import APIRouter,Path

router = APIRouter(prefix="/items")


@router.get("/")
def items_list():
    return [
        "Item1",
        "Item2",
        "Item3"
    ]


@router.get("/latest/")
def get_latest_item():
    return {"id" : "0", "name": "latest"}


@router.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1)]):
    return {
        'Item': {
            "id" : item_id
        }
    },
