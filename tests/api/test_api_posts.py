import pytest
from utils.api_client import APIClient
from utils.test_data_loader import get_new_posts, get_valid_post_ids

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def api():
    return APIClient(BASE_URL)


@pytest.mark.parametrize("title, body, user_id", get_new_posts())
def test_create_post_returns_201(api, title, body, user_id):
    payload = {"title": title, "body": body, "userId": user_id}
    response = api.post("/posts", payload)
    assert response.status_code == 201


@pytest.mark.parametrize("title, body, user_id", get_new_posts())
def test_create_post_returns_correct_data(api, title, body, user_id):
    payload = {"title": title, "body": body, "userId": user_id}
    response = api.post("/posts", payload)
    data = response.json()
    assert data["title"] == title
    assert data["body"] == body
    assert data["userId"] == user_id
    assert "id" in data


@pytest.mark.parametrize("post_id", get_valid_post_ids())
def test_delete_post_returns_200(api, post_id):
    response = api.delete(f"/posts/{post_id}")
    assert response.status_code == 200


def test_get_all_posts_returns_100(api):
    response = api.get("/posts")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 100


def test_get_posts_by_user(api):
    response = api.get("/posts", params={"userId": 1})
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0
    assert all(post["userId"] == 1 for post in data)