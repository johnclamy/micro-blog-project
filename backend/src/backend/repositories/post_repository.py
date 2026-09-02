from backend.models.posts import Post, PostCreate, PostUpdate
from .post_list import get_all_posts, set_next_post, remove_post


class PostRepository:
    def get_all(self) -> list[Post]:
        return get_all_posts()

    def get_by_id(self, post_id: int) -> Post | None:
        posts = self.get_all()
        return next((post for post in posts if post.id == post_id), None)
    
    def create(self, post_in: PostCreate) -> Post:
        posts = self.get_all()
        new_id = max((post.id for post in posts), default=0) + 1
        new_post = Post(id=new_id, **post_in.model_dump())
        set_next_post(new_post)
        return new_post

    def update(self, post_id: int, post_in: PostUpdate) -> Post | None:
        post = self.get_by_id(post_id)

        if not post:
            return None

        update_data = post_in.model_dump(exclude_unset=True)
        updated_post = post.model_copy(update=update_data)

        # Replace list item
        posts = self.get_all()
        index = posts.index(post)
        posts[index] = updated_post
        return updated_post

    def delete(self, post_id: int) -> bool:
        post = self.get_by_id(post_id)
        
        if not post:
            return False

        remove_post(post)
        return True

        
