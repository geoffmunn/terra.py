import asyncio

import uvloop

from terra_classic_sdk.client.lcd import AsyncLCDClient
from terra_classic_sdk.client.lcd.api.tx import CreateTxOptions
from terra_classic_sdk.core import Coins
from terra_classic_sdk.core.bank import MsgSend
from terra_classic_sdk.key.mnemonic import MnemonicKey


async def with_sem(aw, sem):
    async with sem:
        print(sem)
        return await aw


async def main():
    terra = AsyncLCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com/")
    mk = MnemonicKey(
        mnemonic="index light average senior silent limit usual local involve delay update rack cause inmate wall render magnet common feature laundry exact casual resource hundred"
    )
    awallet = terra.wallet(mk)

    msg = MsgSend(
        "terra1333veey879eeqcff8j3gfcgwt8cfrg9mq20v6f",
        "terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
        Coins(uluna=20),
    )
    print(msg)
    tx = await awallet.create_and_sign_tx(
        CreateTxOptions(
            msgs=[msg],
            gas_prices="0.15uluna",
            gas="63199",  # gas="auto", gas_adjustment=1.1
            fee_denoms=["uluna"],
        )
    )
    print(tx)

    result = await terra.tx.broadcast(tx)
    print(result)
    await terra.session.close()


uvloop.install()
asyncio.run(main())
