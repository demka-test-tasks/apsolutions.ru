from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class PostRemoveItem(BaseModel):
    id: int

    class Config:
        orm_mode = True


class Post(PostRemoveItem):
    pass


class SearchPostItem(BaseModel):
    text: str

    class Config:
        orm_mode = True
