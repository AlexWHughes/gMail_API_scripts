import logging
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ✅ Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_out_of_office_status(user_email):
    """
    Retrieves and displays the current Out of Office settings for a user in Google Workspace.
    - Shows if Out of Office is ON or OFF
    - Prints both plain text and rich text messages (if available)
    """
    logging.info(f"🔍 Checking Out of Office status for: {user_email}")

    # ✅ Define OAuth scope and load credentials
    SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic']
    SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'

    try:
        # 🔑 Authenticate with domain-wide delegation
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        ).with_subject(user_email)

        # 🌍 Connect to the Gmail API
        service = build('gmail', 'v1', credentials=credentials)
        logging.info("✅ Successfully authenticated using service account.")

        # 💾 Retrieve current Out of Office settings
        response = service.users().settings().getVacation(userId='me').execute()

        # 🟢 Display Out of Office status
        if response.get('enableAutoReply', False):
            logging.info("🟢 Out of Office is currently ON.")
            print("\n--- CURRENT OUT OF OFFICE SETTINGS ---")
            print(f"Status: ON")
            print(f"Subject: {response.get('responseSubject', 'Not Set')}")
            print(f"Rich Text Message: {response.get('responseBodyHtml', 'Not Set')}")
            print(f"Only send to contacts: {response.get('restrictToContacts', False)}")
            print(f"Only send within domain: {response.get('restrictToDomain', False)}")
        else:
            logging.info("⚪ Out of Office is currently OFF.")
            print("\n--- CURRENT OUT OF OFFICE SETTINGS ---")
            print("Status: OFF")

    except HttpError as e:
        logging.error(f"❌ HTTP error occurred: {e}")
    except FileNotFoundError as e:
        logging.error(f"❌ Service account JSON file not found: {e}")
    except Exception as e:
        logging.error(f"❌ An unexpected error occurred: {e}")


# 📦 **Example usage**
if __name__ == "__main__":
    user_email = 'user@example.com'
    get_out_of_office_status(user_email)
