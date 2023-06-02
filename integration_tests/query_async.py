import asyncio
import uvloop
import base64
from pathlib import Path

from terra_classic_sdk.client.lcd import AsyncLCDClient
from terra_classic_sdk.core import Coins
from terra_classic_sdk.core.bank import MsgSend
from terra_classic_sdk.util.contract import get_code_id


async def main():
    terra = AsyncLCDClient(
        url="https://terra-classic-lcd.publicnode.com/",
        chain_id="columbus-5",
    )

    result = await terra.tx.tx_infos_by_height(None)
    print(result)


uvloop.install()
asyncio.run(main())
