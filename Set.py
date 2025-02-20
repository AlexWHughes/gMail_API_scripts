import logging
import time
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# ✅ Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def set_out_of_office(user_email, subject, message_html):
    """
    Sets the Out of Office reply for a user in Google Workspace using the Gmail API.
    - Only sets HTML (rich text) message (no plain text fallback).
    - Disables any existing reply before applying new settings.
    - No start/end dates (permanently enabled until turned off).
    """
    logging.info(f"🚀 Attempting to set Out of Office reply for: {user_email}")

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

        # 🛑 Step 1: Disable any existing Out of Office reply
        service.users().settings().updateVacation(
            userId='me', body={'enableAutoReply': False}).execute()
        logging.info("🛑 Existing Out of Office reply disabled.")

        # Pause briefly to ensure settings propagate
        time.sleep(3)

        # 💾 Step 2: Construct the new Out of Office settings
        vacation_settings = {
            'enableAutoReply': True,                      # Enable auto-reply
            'responseSubject': subject,                   # Email subject line
            'responseBodyHtml': message_html,             # Rich text message
            'restrictToContacts': False,                  # Send to everyone
            'restrictToDomain': False                     # Send outside domain as well
        }

        # Step 3: Apply the settings using Gmail API
        response = service.users().settings().updateVacation(
            userId='me', body=vacation_settings).execute()

        # ✅ Log success and print response
        logging.info(f"✅ Out of Office reply set successfully for {user_email}.")
        logging.info(f"Response: {response}")

    except HttpError as e:
        logging.error(f"❌ HTTP error occurred: {e}")
    except FileNotFoundError as e:
        logging.error(f"❌ Service account JSON file not found: {e}")
    except Exception as e:
        logging.error(f"❌ An unexpected error occurred: {e}")


# 📦 **Example usage**
if __name__ == "__main__":
    user_email = 'user@example.com'
    subject = 'Out of Office'
    message_html = """
    <p><b>Hello,</b></p>
    <p>Thank you for your email. I am currently out of the office and will respond upon my return.</p>
    <p>Should your enquiry be urgent, please call the office or email our support team at 
    <a href="mailto:support@example.com">support@example.com</a>.</p>
    """

    # Call the function
    set_out_of_office(user_email, subject, message_html)
