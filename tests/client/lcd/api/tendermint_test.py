from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)


def test_validator_set():
    result = terra.tendermint.validator_set()
    print(result)


def test_validator_set_with_height():
    result = terra.tendermint.validator_set(14513401)
    print(result)


def test_node_info():
    result = terra.tendermint.node_info()
    assert result["default_node_info"]["network"] == "columbus-5"


def test_block_info():
    result = terra.tendermint.block_info()
    print(result["block"]["header"]["height"])


def test_block_info_with_height():
    result = terra.tendermint.block_info(14513401)
    print(result)


def test_syncing():
    result = terra.tendermint.syncing()
    print(result)
