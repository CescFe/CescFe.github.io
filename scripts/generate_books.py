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
    "img": str,
    "filename": str
}


def validate_json_structure(data):
    for book in data:
        for field, field_type in required_fields.items():
            if field not in book:
                return False, f"Field {field} is missing in book {book}"
            if not isinstance(book[field], field_type):
                return False, f"Field {field} in book {book} should be of type {field_type.__name__}"
    return True, "All checks passed"


def create_book_md(books, output_dir='../_books'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    created_files = []
    for book in books:
        file_name = f"{book['filename']}.md"
        file_path = os.path.join(output_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"---\n")
            for field, value in book.items():
                if field != "filename":  # Exclude the filename field
                    file.write(f"{field}: {value}\n")
            file.write(f"---\n")
    return created_files


def main():
    books_json_path = get_books_json_path()
    if not file_exists(books_json_path):
        print(f"Error: {books_json_path} does not exist.")
        return

    books_data = load_json(books_json_path)
    valid, message = validate_json_structure(books_data)
    if not valid:
        print(f"Error: {message}")
        return

    created_files = create_book_md(books_data)
    print(f"Created {len(created_files)} markdown files in './_books'")


if __name__ == "__main__":
    main()
