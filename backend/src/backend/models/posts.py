from pydantic import BaseModel, Field
from datetime import date


# Schema for defining a post (id is auto-generated)
class Post(BaseModel):
    id: int = Field(..., description='Unique post identifier')
    author: str = Field(..., max_length=50)
    title: str = Field(..., max_length=100)
    content: str
    date_posted: date


# Schema for creating a new post
class PostCreate(BaseModel):
    author: str = Field(..., max_length=50)
    title: str = Field(..., max_length=100)
    content: str
    date_posted: date


# Schema for updating a post (all fields optional)
class PostUpdate(BaseModel):
    author: str | None = Field(default=None, max_length=50)
    title: str | None = Field(default=None, max_length=100)
    content: str | None = None
    date_posted: date | None = None
