import asyncio

from GSSender.servises import send


async def google_sender(spreadsheetid, values):
    await send(spreadsheetid, values)


def asyncio_sender(spreadsheetid, values):
    asyncio.get_event_loop().run_until_complete(
        google_sender(spreadsheetid, values))


if __name__ == "__main__":
    spreadsheetid = '1v-6Ky1r23LyDGsBZEJ4vwtjncQIneeIP9uVYkZxkyyc'
    # values = [[1], [2], [3], [4], [5]]
    values = [
        ['qwerty'],
        ['asd'],
        ['zxc'],
        ['sd'],
        ['xcvxvb'],
        ['dgdgj'],
        ['vnmvnm'],
        ['24524626256'],
        ['sfgfgx'],
        ['xvbxvb'],
        ['xvnxbn'],
        [1389418945671496570164751],
    ]

    asyncio_sender(spreadsheetid, values)
