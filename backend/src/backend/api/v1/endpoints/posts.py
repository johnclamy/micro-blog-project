from fastapi import APIRouter
from backend.models.posts import Post
from backend.repositories.post_list import get_all_posts


router = APIRouter()


@router.get('/', response_model=list[Post])
async def read_posts():
    return get_all_posts()
