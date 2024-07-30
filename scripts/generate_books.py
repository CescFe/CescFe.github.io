import json
import os


def get_books_json_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(script_dir, 'resources')
    return os.path.join(resources_dir, 'books.json')


def file_exists(file_path):
    return os.path.exists(file_path)


def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        exit(1)


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


def ensure_output_dir_exists(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def create_book_md_content(book):
    content = ["---"]
    for field, value in book.items():
        if field != "filename":  # Exclude the filename field
            content.append(f"{field}: {value}")
    content.append("---")
    content.append("")  # Add an extra blank line at the end
    return "\n".join(content)


def write_markdown_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as md_file:
        md_file.write(content)
        print(f"Created {filename}")


def generate_book_markdown_files(books, output_dir):
    ensure_output_dir_exists(output_dir)
    created_files = []
    for book in books:
        file_name = f"{book['filename']}.md"
        file_path = os.path.join(output_dir, file_name)
        if not os.path.exists(file_path):
            content = create_book_md_content(book)
            write_markdown_file(file_path, content)
            created_files.append(file_path)
        else:
            print(f"Skipped {file_path} (already exists)")
    return created_files


def main():
    books_json_path = get_books_json_path()
    books_output_dir = os.path.join('..', '_books')

    print(f"Using JSON file for books: {books_json_path}")
    print(f"Output directory for books: {books_output_dir}")

    books_data = load_json(books_json_path)
    generate_book_markdown_files(books_data, books_output_dir)


if __name__ == "__main__":
    main()
