from typing import Union

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from workout_api.routers import api_router

app = FastAPI(title="WorkoutApi")
app.include_router(api_router)
add_pagination(app)

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
