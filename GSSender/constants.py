import os

from dotenv import load_dotenv

load_dotenv()

LOGGING_LEVEL = os.environ['LOGGING_LEVEL']
CREDENTIALS_TYPE = os.environ['CREDENTIALS_TYPE']
SPREADSHEETS_URL = 'https://docs.google.com/spreadsheets/d/{0}'
SCOPES = (
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
)

EMAIL_USER = os.environ['EMAIL']


match CREDENTIALS_TYPE:
    case "json":
        INFO = os.environ['CREDENTIALS_JSON_PATH']
    case "env":
        INFO = {
            'type':  os.environ['TYPE'],
            'project_id':  os.environ['PROJECT_ID'],
            'private_key_id':  os.environ['PRIVATE_KEY_ID'],
            'private_key':  os.environ['PRIVATE_KEY'],
            'client_email':  os.environ['CLIENT_EMAIL'],
            'client_id':  os.environ['CLIENT_ID'],
            'auth_uri':  os.environ['AUTH_URI'],
            'token_uri':  os.environ['TOKEN_URI'],
            'auth_provider_x509_cert_url':  os.environ[
                'AUTH_PROVIDER_X509_CERT_URL'],
            'client_x509_cert_url':  os.environ['CLIENT_X509_CERT_URL']
        }
    case _:
        print("Code not found")
