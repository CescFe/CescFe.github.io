import shutil

import pytest
import os
from scripts.generate_books import file_exists, load_json, validate_json_structure, create_book_md


@pytest.fixture
def sample_books_json_path():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(test_dir, 'resources', 'books')
    sample_json_path = os.path.join(resources_dir, 'sample_books.json')
    return sample_json_path


@pytest.fixture
def source_books_json_path():
    source_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(source_dir, '..', 'assets', 'json')
    source_json_path = os.path.join(resources_dir, 'books.json')
    return source_json_path


def test_access_books_json(sample_books_json_path):
    assert file_exists(sample_books_json_path), f"File {sample_books_json_path} does not exist."


def test_books_json_is_not_empty(sample_books_json_path):
    sample_data = load_json(sample_books_json_path)
    assert len(sample_data) > 0, f"File {sample_books_json_path} should not be empty"


def test_books_json_is_a_list(sample_books_json_path):
    sample_data = load_json(sample_books_json_path)
    assert isinstance(sample_data, list), f"File {sample_books_json_path} should be a list"


def test_sample_books_json_structure_is_valid(sample_books_json_path):
    sample_data = load_json(sample_books_json_path)
    valid, message = validate_json_structure(sample_data)
    assert valid, message


def test_create_books_md(source_books_json_path):
    books = load_json(source_books_json_path)
    output_dir = './_books'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    created_files = create_book_md(books, output_dir)
    try:
        for file_path in created_files:
            assert os.path.exists(file_path), f"Markdown file {file_path} was not created."
    finally:
        # Clean up the created files after the test
        shutil.rmtree(output_dir)
