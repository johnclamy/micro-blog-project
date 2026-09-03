import pytest
from datetime import date
from fastapi.testclient import TestClient
from backend.main import app
from backend.models.posts import Post
from backend.api.v1.endpoints.posts import get_post_repository
from backend.repositories.post_repository import PostRepository, PostCreate, PostUpdate


# 1. Create an isolated in-memory test repository
class FakePostRepository(PostRepository):
    def __init__(self):
        # Seed with isolated test data for predictable tests
        self._posts = [
            Post(
                id=1,
                author="Test Author",
                title="Test Title 1",
                content="Test Content 1",
                date_posted=date(2026, 1, 1),
            ),
            Post(
                id=2,
                author="Test Author 2",
                title="Test Title 2",
                content="Test Content 2",
                date_posted=date(2026, 1, 2),
            ),
        ]

    def get_all(self) -> list[Post]:
        return self._posts

    def get_by_id(self, post_id: int) -> Post | None:
        return next((p for p in self._posts if p.id == post_id), None)

    def create(self, post_in: PostCreate) -> Post:
        new_id = max((p.id for p in self._posts), default=0) + 1
        new_post = Post(id=new_id, **post_in.model_dump())
        self._posts.append(new_post)
        return new_post

    def update(self, post_id: int, post_in: PostUpdate) -> Post | None:
        post = self.get_by_id(post_id)
        if not post:
            return None
        update_data = post_in.model_dump(exclude_unset=True)
        updated_post = post.model_copy(update=update_data)
        idx = self._posts.index(post)
        self._posts[idx] = updated_post
        return updated_post

    def delete(self, post_id: int) -> bool:
        post = self.get_by_id(post_id)
        if not post:
            return False
        self._posts.remove(post)
        return True


# 2. Pytest fixture providing TestClient with dependency override applied
@pytest.fixture
def client():
    fake_repo = FakePostRepository()

    # Override the real repository dependency with the fake implementation
    app.dependency_overrides[get_post_repository] = lambda: fake_repo

    with TestClient(app) as test_client:
        yield test_client

    # Clean up overrides after test execution
    app.dependency_overrides.clear()