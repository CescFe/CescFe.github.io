import json
import os.path

import pytest


@pytest.fixture
def sample_books_json_path():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(test_dir, 'resources', 'books')
    sample_json_path = os.path.join(resources_dir, 'sample_books.json')
    return sample_json_path


def test_access_books_json(sample_books_json_path):
    assert os.path.exists(sample_books_json_path), f"File {sample_books_json_path} does not exist."


def test_books_json_is_not_empty(sample_books_json_path):
    with open(sample_books_json_path, 'r', encoding='utf-8') as file:
        sample_data = json.load(file)
        assert len(sample_data) > 0, f"File {sample_books_json_path} should not be empty"


def test_books_json_is_a_list(sample_books_json_path):
    with open(sample_books_json_path, 'r', encoding='utf-8') as file:
        sample_data = json.load(file)
        assert isinstance(sample_data, list), f"File {sample_books_json_path} should be a list"


def test_sample_books_json_structure_is_valid(sample_books_json_path):
    required_fields = {
        "layout": str,
        "title": str,
        "author": str,
        "isbn": str,
        "pvp": str,
        "year": int,
        "description": str,
        "description_long": str,
        "importance": int,
        "category": str,
        "img": str
    }
    with (open(sample_books_json_path, 'r', encoding='utf-8') as file):
        sample_data = json.load(file)
        for book in sample_data:
            for field, field_type in required_fields.items():
                assert field in book, f"Field {field} is missing in book {book}"
                assert isinstance(book[field], field_type),f"Field {field} in book {book} should be of type {field_type.__name__}"
