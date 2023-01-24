from aiogoogle.auth.creds import ServiceAccountCreds

from .constants import INFO, SCOPES

creds = ServiceAccountCreds(scopes=SCOPES, **INFO)
