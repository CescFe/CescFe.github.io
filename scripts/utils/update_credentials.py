import os
from dotenv import load_dotenv
import json

load_dotenv()

CLIENT_ID_DENES_SHEET = os.getenv('CLIENT_ID_DENES_SHEET')
CLIENT_SECRET_DENES_SHEET = os.getenv('CLIENT_SECRET_DENES_SHEET')


def update_credentials():
    if not CLIENT_ID_DENES_SHEET or not CLIENT_SECRET_DENES_SHEET:
        raise ValueError("Missing CLIENT_ID_DENES_SHEET or CLIENT_SECRET_DENES_SHEET environment variables")

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(script_dir, 'credentials.json')

    # Load the existing credentials.json template
    with open(credentials_path, 'r', encoding='utf-8') as file:
        credentials = json.load(file)

    # Update the CLIENT_ID_DENES_SHEET and CLIENT_SECRET_DENES_SHEET
    credentials['installed']['client_id'] = CLIENT_ID_DENES_SHEET
    credentials['installed']['client_secret'] = CLIENT_SECRET_DENES_SHEET

    # Save the updated credentials back to the file
    with open(credentials_path, 'w', encoding='utf-8') as file:
        json.dump(credentials, file, indent=4, ensure_ascii=False)

    print("Updated credentials.json with environment variables")


if __name__ == "__main__":
    update_credentials()
