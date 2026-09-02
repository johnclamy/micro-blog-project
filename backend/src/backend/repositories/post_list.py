from datetime import date
from backend.models.posts import Post


_posts: list[Post] = [
    Post(
        id=1,
        author="Jane Doe",
        title="Getting Started with FastAPI",
        content="FastAPI is a modern, fast web framework...",
        date_posted=date(2026, 8, 15),
    ),
    Post(
        id=2,
        author="John Smith",
        title="Understanding Pydantic Models",
        content="Pydantic provides data validation...",
        date_posted=date(2026, 8, 20),
    ),
    Post(
        id=3,
        author="Alice Johnson",
        title="Pythonic Code Patterns",
        content="Writing pythonic code means...",
        date_posted=date(2026, 8, 28),
    ),
    Post(
        id=4,
        author="Bob Wilson",
        title="Async Programming in Python",
        content="Asynchronous execution allows...",
        date_posted=date(2026, 9, 1),
    ),
]


def get_all_posts() -> list[Post]:
    return _posts
