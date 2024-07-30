import json
import os


def get_collections_json_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resources_dir = os.path.join(script_dir, 'resources')
    return os.path.join(resources_dir, 'collections.json')


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
    "description": str,
    "img": str,
    "importance": int,
    "category": str,
    "category_book": str,
    "related_publications": bool,
    "horizontal": bool,
    "filename": str
}


def validate_json_structure(data):
    for collection in data:
        for field, field_type in required_fields.items():
            if field not in collection:
                return False, f"Field {field} is missing in collection {collection}"
            if not isinstance(collection[field], field_type):
                return False, f"Field {field} in collection {collection} should be of type {field_type.__name__}"
    return True, "All checks passed"


def ensure_output_dir_exists(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def create_collection_md_content(collection):
    content = ["---"]
    for field, value in collection.items():
        if field != "filename":  # Exclude the filename field
            if isinstance(value, bool):
                value = str(value).lower()  # Convert boolean to lowercase string
            content.append(f"{field}: {value}")
    content.append("---")
    content.append("")
    content.append("{% include books_display.liquid %}")
    content.append("")  # Add an extra blank line at the end
    return "\n".join(content)


def write_markdown_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as md_file:
        md_file.write(content)
        print(f"Created {filename}")


def generate_collection_markdown_files(collections, output_dir):
    ensure_output_dir_exists(output_dir)
    created_files = []
    for collection in collections:
        file_name = f"{collection['filename']}.md"
        file_path = os.path.join(output_dir, file_name)
        if not os.path.exists(file_path):
            content = create_collection_md_content(collection)
            write_markdown_file(file_path, content)
            created_files.append(file_path)
        else:
            print(f"Skipped {file_path} (already exists)")
    return created_files


def main():
    collections_json_path = get_collections_json_path()
    collections_output_dir = os.path.join('..', '_collections')

    print(f"Using JSON file for collections: {collections_json_path}")
    print(f"Output directory for collections: {collections_output_dir}")

    collections_data = load_json(collections_json_path)
    generate_collection_markdown_files(collections_data, collections_output_dir)


if __name__ == "__main__":
    main()
