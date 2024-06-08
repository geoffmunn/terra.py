from terra_classic_sdk.client.lcd import LCDClient
from terra_classic_sdk.client.lcd.params import PaginationOptions

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_tx_info():
    result = terra.tx.tx_info(
        "A247772DC239530F9F1198A6ECFBD2C1856BA4E35EC68D3BE962461952059AC8"
    )
    assert result is not None


def test_search():
    result = terra.tx.search(
        [
            ("tx.height", 16771543),
            ("message.sender", "terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9"),
        ]
    )
    assert result is not None
    assert len(result) > 0


def test_tx_infos_by_height():
    result = terra.tx.tx_infos_by_height()
    assert result is not None


def test_tx_infos_by_height_with_height():
    result = terra.tx.tx_infos_by_height(16771543)
    assert result is not None
