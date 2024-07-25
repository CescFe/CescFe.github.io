import json
import os


def get_books_json_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, '..', 'assets', 'json')
    return os.path.join(assets_dir, 'books.json')


def file_exists(file_path):
    return os.path.exists(file_path)


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def validate_json_structure(data):
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
    for book in data:
        for field, field_type in required_fields.items():
            if field not in book:
                return False, f"Field {field} is missing in book {book}"
            if not isinstance(book[field], field_type):
                return False, f"Field {field} in book {book} should be of type {field_type.__name__}"
    return True, "All checks passed"
