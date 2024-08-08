import os
import json
from dotenv import load_dotenv


def check_environment_variables(client_id_denes_sheet, client_secret_denes_sheet):
    if not client_id_denes_sheet or not client_secret_denes_sheet:
        raise ValueError("Missing client_id_denes_sheet or client_secret_denes_sheet environment variables")


def get_absolute_path(credentials_relative_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(script_dir, credentials_relative_path)
    return credentials_path


def load_credentials(credentials_path):
    with open(credentials_path, 'r', encoding='utf-8') as file:
        credentials = json.load(file)
        return credentials


def update_credentials_data(credentials, client_id_denes_sheet, client_secret_denes_sheet):
    credentials['installed']['client_id'] = client_id_denes_sheet
    credentials['installed']['client_secret'] = client_secret_denes_sheet


def save_credentials(credentials, credentials_path):
    with open(credentials_path, 'w', encoding='utf-8') as file:
        json.dump(credentials, file, indent=4, ensure_ascii=False)
    print("Updated credentials.json with environment variables")


def update_credentials(client_id_denes_sheet, client_secret_denes_sheet, credentials_path):
    check_environment_variables(client_id_denes_sheet, client_secret_denes_sheet)
    credentials = load_credentials(credentials_path)
    update_credentials_data(credentials, client_id_denes_sheet, client_secret_denes_sheet)
    save_credentials(credentials, credentials_path)


def main():
    load_dotenv()
    credentials_relative_path = "credentials.json"
    client_id_denes_sheet = os.getenv('CLIENT_ID_DENES_SHEET')
    client_secret_denes_sheet = os.getenv('CLIENT_SECRET_DENES_SHEET')
    credentials_path = get_absolute_path(credentials_relative_path)
    update_credentials(client_id_denes_sheet, client_secret_denes_sheet, credentials_path)


if __name__ == "__main__":
    main()
