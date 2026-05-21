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