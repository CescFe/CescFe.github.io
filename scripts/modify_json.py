import json
import os
import random
import string


def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def generate_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def add_filename_field(data):
    for item in data:
        item['filename'] = generate_random_string()
    return data


def main():
    # Use raw string (r) to avoid issues with backslashes
    input_file_path = r'C:\Users\dotae\PycharmProjects\CescFe.github.io\tests\resources\books\sample_books.json'
    output_file_path = r'C:\Users\dotae\PycharmProjects\CescFe.github.io\tests\resources\books\sample_books.json'

    data = load_json(input_file_path)
    modified_data = add_filename_field(data)
    save_json(modified_data, output_file_path)
    print(f"Modified JSON has been saved to {output_file_path}")


if __name__ == "__main__":
    main()
