from fastapi import APIRouter
from backend.models.posts import Post
from backend.repositories.post_repository import (
    PostCreate,
    PostRepository,
    PostUpdate,
)


router = APIRouter()
repo = PostRepository()


@router.get('/', response_model=list[Post])
async def read_posts():
    """Retrieve all posts."""
    return repo.get_all()


@router.get('/{post_id}', response_model=Post)
async def read_post(post_id: int):
    """Retrieve a single post by ID."""
    post = repo.get_by_id(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {post_id} not found",
        )
    return post


@router.post('/', response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post_in: PostCreate):
    """Create a new post."""
    return repo.create(post_in)


@router.patch('/{post_id}', response_model=Post)
async def update_post(post_id: int, post_in: PostUpdate):
    """Partially update an existing post."""
    updated_post = repo.update(post_id, post_in)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {post_id} not found",
        )
    return updated_post


@router.delete('/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int):
    """Delete a post by ID."""
    deleted = repo.delete(post_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {post_id} not found",
        )
    return None
