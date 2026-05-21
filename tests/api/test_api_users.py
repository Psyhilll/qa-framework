import pytest
from utils.api_client import APIClient
from utils.test_data_loader import get_valid_user_ids, get_invalid_user_ids

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def api():
    return APIClient(BASE_URL)


@pytest.mark.parametrize("user_id", get_valid_user_ids())
def test_get_user_returns_200(api, user_id):
    response = api.get(f"/users/{user_id}")
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", get_valid_user_ids())
def test_get_user_returns_correct_id(api, user_id):
    response = api.get(f"/users/{user_id}")
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.parametrize("user_id", get_valid_user_ids())
def test_get_user_has_required_fields(api, user_id):
    response = api.get(f"/users/{user_id}")
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "username" in data


@pytest.mark.parametrize("user_id", get_invalid_user_ids())
def test_get_nonexistent_user_returns_404(api, user_id):
    response = api.get(f"/users/{user_id}")
    assert response.status_code == 404