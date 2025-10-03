import asyncio

import uvloop

from terra_classic_sdk.client.lcd import AsyncLCDClient


async def with_sem(aw, sem):
    async with sem:
        print(sem)
        return await aw


async def main():
    terra = AsyncLCDClient(url="https://terra-classic-lcd.publicnode.com", chain_id="columbus-5")
    validators, _ = await terra.staking.validators()
    validator_addresses = [v.operator_address for v in validators]

    sem = asyncio.Semaphore(2)  # 2 continuous connections
    result = await asyncio.gather(
        *[
            with_sem(terra.oracle.misses(address), sem)
            for address in validator_addresses
        ]
    )

    await terra.session.close()
    print(result)


uvloop.install()
asyncio.run(main())
