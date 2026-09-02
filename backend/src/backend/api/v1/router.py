from fastapi import APIRouter
from backend.api.v1.endpoints import posts


api_router = APIRouter()


# Prefixes all routes inside posts.py with /posts
api_router.include_router(posts.router, prefix='/posts', tags=['Posts'])
