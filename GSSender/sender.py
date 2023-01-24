import asyncio

from GSSender.servises import send


async def google_sender(spreadsheetid, values):
    await send(spreadsheetid, values)


def asyncio_sender(spreadsheetid, values):
    asyncio.get_event_loop().run_until_complete(
        google_sender(spreadsheetid, values))
