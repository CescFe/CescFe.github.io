import os
import json

CLIENT_ID_DENES_SHEET = os.environ.get('CLIENT_ID_DENES_SHEET')
CLIENT_SECRET_DENES_SHEET = os.environ.get('CLIENT_SECRET_DENES_SHEET')


def update_credentials():
    if not CLIENT_ID_DENES_SHEET or not CLIENT_SECRET_DENES_SHEET:
        raise ValueError("Missing CLIENT_ID_DENES_SHEET or CLIENT_SECRET_DENES_SHEET environment variables")

    # Load the existing credentials.json template
    with open('credentials.json', 'r', encoding='utf-8') as file:
        credentials = json.load(file)

    # Update the CLIENT_ID_DENES_SHEET and CLIENT_SECRET_DENES_SHEET
    credentials['installed']['CLIENT_ID_DENES_SHEET'] = CLIENT_ID_DENES_SHEET
    credentials['installed']['CLIENT_SECRET_DENES_SHEET'] = CLIENT_SECRET_DENES_SHEET

    # Save the updated credentials back to the file
    with open('credentials.json', 'w', encoding='utf-8') as file:
        json.dump(credentials, file, indent=4, ensure_ascii=False)

    print("Updated credentials.json with environment variables")


if __name__ == "__main__":
    update_credentials()
