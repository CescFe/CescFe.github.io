import os.path
import json
from dotenv import load_dotenv

from utils.credentials_sheet_handler import update_credentials, get_absolute_path
from utils.google_libs_handler import get_credentials, fetch_sheet_data

load_dotenv()
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
DENES_SPREADSHEET_ID = os.environ.get('DENES_SPREADSHEET_ID')
FETCH_RANGE = "collections"
CLIENT_ID_DENES_SHEET = os.environ.get('CLIENT_ID_DENES_SHEET')
CLIENT_SECRET_DENES_SHEET = os.environ.get('CLIENT_SECRET_DENES_SHEET')
CREDENTIALS_FILENAME = "credentials.json"
TOKEN_FILENAME = "token.json"
OUTPUT_COLLECTIONS_FILE = "collections.json"


def transform_to_json(values):
    if not values:
        print("No data found.")
        return []

    header = values[0]
    data = []
    # Transform rows into a list of dictionaries
    for row in values[1:]:
        row_data = {header[i]: row[i] if i < len(row) else "" for i in range(len(header))}
        data.append(row_data)
    return data


def write_to_file(data, filename):
    with open(filename, "w", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    print(f"Data has been written to {filename}")


def main():
    credentials_path = get_absolute_path(CREDENTIALS_FILENAME)
    update_credentials(CLIENT_ID_DENES_SHEET, CLIENT_SECRET_DENES_SHEET, credentials_path)
    credentials = get_credentials(credentials_path, get_absolute_path(TOKEN_FILENAME), SCOPES)

    values = fetch_sheet_data(credentials, DENES_SPREADSHEET_ID, FETCH_RANGE)
    data = transform_to_json(values)
    write_to_file(data, OUTPUT_COLLECTIONS_FILE)


if __name__ == "__main__":
    main()
