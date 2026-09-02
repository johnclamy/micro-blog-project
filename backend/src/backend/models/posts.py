from pydantic import BaseModel, Field
from datetime import date


class Post(BaseModel):
    id: int = Field(..., description='Unique post identifier')
    author: str = Field(..., max_length=50)
    title: str = Field(..., max_length=100)
    content: str
    date_posted: date
