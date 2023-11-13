Usage with asyncio
==================
    
You can use AsyncLCDClient to make asynchronous, non-blocking LCD requests.
The interface is similar to LCDClient, except the module and wallet API functions must be awaited.

Async module APIs
-----------------

You can replace your LCDClient instance with AsyncLCDClient inside a coroutine function:

.. code-block:: python

    import asyncio 
    from terra_classic_sdk.client.lcd import AsyncLCDClient

    async def main():
        terra = AsyncLCDClient("https://terra-classic-lcd.publicnode.com", "columbus-5")
        total_supply = await terra.bank.total()
        print(total_supply)
        await terra.session.close() # you must close the session

    asyncio.run(main())


For convenience, you can use the async context manager to automatically teardown the
session. Here's the same code as above, this time using the ``async with`` construct.

.. code-block:: python

    import asyncio 
    from terra_classic_sdk.client.lcd import AsyncLCDClient

    async def main():
        async with AsyncLCDClient("https://terra-classic-lcd.publicnode.com", "columbus-5") as terra:
            total_supply = await terra.bank.total()
            print(total_supply)

    asyncio.run(main())

Async wallet API
----------------

When creating a wallet with AsyncLCDClient, the wallet's methods that create LCD requests
are also asychronous and therefore must be awaited.

.. code-block:: python

    import asyncio
    from terra_classic_sdk.client.lcd.api.tx import CreateTxOptions
    from terra_classic_sdk.client.lcd import AsyncLCDClient
    from terra_classic_sdk.core.bank import MsgSend
    from terra_classic_sdk.key.mnemonic import MnemonicKey
    from terra_classic_sdk.core import Coins
    from terra_classic_sdk.core.tx import Tx

    mk = MnemonicKey(mnemonic='secret 24 word phrase')
    recipient = "terra..."

    async def main():
        async with AsyncLCDClient("https://terra-classic-lcd.publicnode.com", "columbus-5") as terra:
            wallet = terra.wallet(mk)
            tx:Tx = await wallet.create_and_sign_tx(
                CreateTxOptions(
                    msgs=[MsgSend(wallet.key.acc_address, recipient, Coins(uluna=100000000))]
                )
            )

            print (tx.auth_info.fee)

    asyncio.run(main())

Alternative event loops
-----------------------

The native ``asyncio`` event loop can be replaced with an alternative such as ``uvloop``
for more performance. For example:

.. code-block:: python

    import asyncio
    import uvloop
    from terra_classic_sdk.client.lcd.api.tx import CreateTxOptions
    from terra_classic_sdk.client.lcd import AsyncLCDClient
    from terra_classic_sdk.core.bank import MsgSend
    from terra_classic_sdk.key.mnemonic import MnemonicKey
    from terra_classic_sdk.core import Coins
    from terra_classic_sdk.core.tx import Tx

    mk = MnemonicKey(mnemonic='secret 24 word phrase')
    recipient = "terra..."

    async def main():
        async with AsyncLCDClient("https://terra-classic-lcd.publicnode.com", "columbus-5") as terra:
            wallet = terra.wallet(mk)
            tx:Tx = await wallet.create_and_sign_tx(
                CreateTxOptions(
                    msgs=[MsgSend(wallet.key.acc_address, recipient, Coins(uluna=100000000))]
                )
            )

            print (tx.auth_info.fee)

    uvloop.install()
    asyncio.run(main())
