import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

COLLECTIONS_DENES_SHEET_ID = "1q_ityTPJaBxxmANQawi4Kjamq5wIVoQkahLsp63rP7g"
RANGE = "Sheet1"


def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=COLLECTIONS_DENES_SHEET_ID, range=RANGE).execute()

        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        # Extract header
        header = values[0]
        data = []

        # Transform rows into a list of dictionaries
        for row in values[1:]:
            row_data = {header[i]: row[i] if i < len(row) else "" for i in range(len(header))}
            data.append(row_data)

        # Write data to collections.json file
        with open("collections.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        print("Data has been written to collections.json")

    except HttpError as error:
        print(error)


if __name__ == "__main__":
    main()
