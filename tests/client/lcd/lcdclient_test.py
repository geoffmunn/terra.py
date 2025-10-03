import asynctest
from aioresponses import aioresponses

from terra_classic_sdk.client.lcd import AsyncLCDClient, LCDClient

"""
class TestDoSessionGet(asynctest.TestCase):
    @aioresponses()
    def test_makes_request_to_expected_url(self, mocked):
        mocked.get(
            "https://terra-classic-lcd.publicnode.com/cosmos/base/tendermint/v1beta1/node_info",
            status=200,
            body='{"response": "test"}',
        )
        terra = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com/")

        resp = terra.tendermint.node_info()
        assert resp == {"response": "test"}
        terra.session.close()

    @aioresponses()
    async def test_makes_request_to_expected_url_async(self, mocked):
        mocked.get(
            "https://terra-classic-lcd.publicnode.com/cosmos/base/tendermint/v1beta1/node_info",
            status=200,
            body='{"response": "test"}',
        )
        terra = AsyncLCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com/")

        resp = await terra.tendermint.node_info()
        print(resp)
        assert resp == {"response": "test"}
        terra.session.close()


if __name__ == "__main__":
    asynctest.main()
"""
