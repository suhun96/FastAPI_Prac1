from pydantic import BaseModel
from typing import Optional 

class MemoCreated(BaseModel):
    title : str
    content : str
    is_favorite : bool

    class Config:
        orm_mode = True

class MemoRequestCreate(BaseModel):
    title : str
    content : Optional[str] = None
    is_favorite : Optional[bool] = False

class UserCreated(BaseModel):
    name : str