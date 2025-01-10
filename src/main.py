from typing import TypedDict
import fastapi

class ItemResponse(TypedDict):
    item_id: int
    q: str | None

app = fastapi.FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> ItemResponse | None:
    return {"item_id": item_id, "q": q}

