import os.path
import json
from dotenv import load_dotenv

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from utils.credentials_sheet_handler import update_credentials, get_absolute_path

load_dotenv()
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
DENES_SPREADSHEET_ID = os.environ.get('DENES_SPREADSHEET_ID')
FETCH_RANGE = "collections"
CLIENT_ID_DENES_SHEET = os.environ.get('CLIENT_ID_DENES_SHEET')
CLIENT_SECRET_DENES_SHEET = os.environ.get('CLIENT_SECRET_DENES_SHEET')
CREDENTIALS_FILENAME = "credentials.json"
TOKEN_FILENAME = "token.json"
OUTPUT_COLLECTIONS_FILE = "collections.json"


def get_credentials(credentials_path, token_path):
    credentials = None
    if os.path.exists(get_absolute_path(TOKEN_FILENAME)):
        credentials = Credentials.from_authorized_user_file(get_absolute_path(TOKEN_FILENAME), SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            credentials = flow.run_local_server(port=0)
        with open(token_path, "w") as token:
            token.write(credentials.to_json())
    return credentials


def fetch_sheet_data(credentials, spreadsheet_id, fetch_range):
    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId=spreadsheet_id, range=fetch_range).execute()
        return result.get("values", [])
    except HttpError as error:
        print(error)


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

    token_path = get_absolute_path(TOKEN_FILENAME)

    credentials = get_credentials(credentials_path, token_path)
    values = fetch_sheet_data(credentials, DENES_SPREADSHEET_ID, FETCH_RANGE)
    data = transform_to_json(values)
    write_to_file(data, OUTPUT_COLLECTIONS_FILE)


if __name__ == "__main__":
    main()
