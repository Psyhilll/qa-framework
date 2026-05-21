import json
import os
import pytest


def load_login_data():
    data_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "login_data.json")
    with open(data_path, "r") as f:
        return json.load(f)


def get_valid_users():
    data = load_login_data()
    return [
        pytest.param(user["username"], user["password"], user["expected_url"], id=user["test_id"])
        for user in data["valid_users"]
    ]


def get_invalid_users():
    data = load_login_data()
    return [
        pytest.param(user["username"], user["password"], user["expected_error"], id=user["test_id"])
        for user in data["invalid_users"]
    ]
def load_api_data():
    data_path = os.path.join(os.path.dirname(__file__), "..", "test_data", "api_data.json")
    with open(data_path, "r") as f:
        return json.load(f)


def get_valid_user_ids():
    data = load_api_data()
    return [
        pytest.param(entry["user_id"], id=entry["test_id"])
        for entry in data["valid_user_ids"]
    ]


def get_invalid_user_ids():
    data = load_api_data()
    return [
        pytest.param(entry["user_id"], id=entry["test_id"])
        for entry in data["invalid_user_ids"]
    ]


def get_new_posts():
    data = load_api_data()
    return [
        pytest.param(entry["title"], entry["body"], entry["userId"], id=entry["test_id"])
        for entry in data["new_posts"]
    ]


def get_valid_post_ids():
    data = load_api_data()
    return [
        pytest.param(entry["post_id"], id=entry["test_id"])
        for entry in data["valid_post_ids"]
    ]