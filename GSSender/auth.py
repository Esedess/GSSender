from aiogoogle.auth.creds import ServiceAccountCreds

from .constants import CREDENTIALS_TYPE, INFO, SCOPES

match CREDENTIALS_TYPE:
    case "json":
        import json
        service_account_keys = json.load(open(INFO))
    case "env":
        service_account_keys = INFO

creds = ServiceAccountCreds(scopes=SCOPES, **service_account_keys)
