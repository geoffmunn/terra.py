from terra_classic_sdk.client.lcd import LCDClient
from terra_classic_sdk.client.lcd.params import PaginationOptions

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)
pagOpt = PaginationOptions(limit=2, count_total=True)

def test_balance():
    result, _ = terra.bank.balance(address ="terra1kgge7tyctna52qfskpkw73xu4fhmd0y29ravr6")

    assert result.to_data()
    assert result.get("uluna").amount > 0

def test_balance_with_pagination():
    result, _   = terra.bank.balance(
        address = "terra1kgge7tyctna52qfskpkw73xu4fhmd0y29ravr6", params=pagOpt
    )
    assert result.to_data()


def test_total():
    result, _ = terra.bank.total()
    assert result.to_data()


def test_total_with_pagination():
    result, _ = terra.bank.total(pagOpt)
    assert result.to_data()
