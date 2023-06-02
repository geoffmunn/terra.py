from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)


def test_parameters():
    result = terra.ibc_transfer.parameters()
    assert result.get("send_enabled")
    assert result.get("receive_enabled")
