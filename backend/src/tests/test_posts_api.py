from fastapi import status


def test_read_posts(client):
    """Test retrieving all posts."""
    response = client.get("/api/v1/posts/")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Test Title 1"


def test_read_post_success(client):
    """Test retrieving a single post by ID."""
    response = client.get("/api/v1/posts/1")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == 1
    assert data["author"] == "Test Author"


def test_read_post_not_found(client):
    """Test retrieving a non-existent post return 404."""
    response = client.get("/api/v1/posts/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["detail"] == "Post with ID 999 not found"


def test_create_post(client):
    """Test creating a new post."""
    payload = {
        "author": "New Writer",
        "title": "Brand New Post",
        "content": "Exciting content goes here.",
        "date_posted": "2026-09-03",
    }
    response = client.post("/api/v1/posts/", json=payload)

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["id"] == 3
    assert data["title"] == "Brand New Post"


def test_update_post(client):
    """Test updating fields of an existing post."""
    payload = {"title": "Updated Title Standard"}
    response = client.patch("/api/v1/posts/1", json=payload)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Updated Title Standard"
    assert data["author"] == "Test Author"  # Unchanged field remains intact


def test_delete_post(client):
    """Test deleting a post and verifying it no longer exists."""
    delete_response = client.delete("/api/v1/posts/1")
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    # Verify retrieval returns 404 after deletion
    get_response = client.get("/api/v1/posts/1")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND