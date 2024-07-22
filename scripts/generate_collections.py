import json
import os


class CollectionMarkdownGenerator:
    def __init__(self, json_path, output_dir):
        self.json_path = json_path
        self.output_dir = output_dir

    def load_collections(self):
        try:
            with open(self.json_path, 'r') as file:
                collections = json.load(file)
            return collections
        except FileNotFoundError:
            print(f"Error: The file '{self.json_path}' was not found.")
            exit(1)
        except json.JSONDecodeError:
            print(f"Error: The file '{self.json_path}' is not a valid JSON file.")
            exit(1)

    @staticmethod
    def create_markdown_content(collection):
        return f"""---
layout: {collection['layout']}
title: {collection['title']}
description: {collection['description']}
img: {collection['img']}
importance: {collection['importance']}
category: {collection['category']}
category_book: {collection['category_book']}
related_publications: {str(collection['related_publications']).lower()}
horizontal: {str(collection['horizontal']).lower()}
---

{{% include books_display.liquid %}}
"""

    def ensure_output_dir_exists(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    @staticmethod
    def write_markdown_file(filename, content):
        with open(filename, 'w') as md_file:
            md_file.write(content)
            print(f"Created {filename}")

    def generate_markdown_files(self):
        self.ensure_output_dir_exists()
        collections = self.load_collections()

        for collection in collections:
            filename = os.path.join(self.output_dir, collection['filename'])
            if not os.path.exists(filename):
                content = self.create_markdown_content(collection)
                self.write_markdown_file(filename, content)
            else:
                print(f"Skipped {filename} (already exists)")


def main():
    # Set the base path to the root of your project
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Use the base path to construct the absolute path for the JSON file
    json_path = os.path.join(base_path, 'assets', 'json', 'collections.json')
    output_dir = os.path.join(base_path, '_collections')

    print(f"Using JSON file: {json_path}")
    print(f"Output directory: {output_dir}")

    generator = CollectionMarkdownGenerator(json_path, output_dir)
    generator.generate_markdown_files()


if __name__ == "__main__":
    main()
