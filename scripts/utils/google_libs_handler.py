import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .credentials_sheet_handler import get_absolute_path


def get_credentials(credentials_path, token_filename, scopes):
    credentials = None
    if os.path.exists(get_absolute_path(token_filename)):
        credentials = Credentials.from_authorized_user_file(get_absolute_path(token_filename), scopes)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)
            credentials = flow.run_local_server(port=0)
        with open(get_absolute_path(token_filename), "w") as token:
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
