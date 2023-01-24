from typing import Any

from aiogoogle import Aiogoogle

from .auth import creds
from .constants import SPREADSHEETS_URL
from .logger import logger


async def spreadsheets_update_value(
        spreadsheetid: str,
        table_values: list[list[Any]],
) -> None:
    async with Aiogoogle(service_account_creds=creds) as aiogoogle:
        service = await aiogoogle.discover('sheets', 'v4')
        range = f'1:{len(table_values)}'

        update_body = {
            'majorDimension': 'COLUMNS',
            'values': table_values
        }
        await aiogoogle.as_service_account(
            service.spreadsheets.values.append(
                spreadsheetId=spreadsheetid,
                range=range,
                valueInputOption='USER_ENTERED',
                json=update_body
            )
        )


async def send(
    spreadsheetid: str,
    values: list[list[Any]],
) -> None:
    await spreadsheets_update_value(spreadsheetid, values)
    logger.info(SPREADSHEETS_URL.format(spreadsheetid))
