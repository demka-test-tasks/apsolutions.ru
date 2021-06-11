from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class PostRemoveItem(BaseModel):
    id: int

    class Config:
        orm_mode = True

# TODO Можно использовать для создания постов
class Post(PostRemoveItem):
    text: str

    class Config:
        orm_mode = True
