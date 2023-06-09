from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)


def test_inflation():
    result = terra.mint.inflation()
    print(result.to_data())


def test_annual_provisions():
    result = terra.mint.annual_provisions()
    print(result.to_data())


def test_parameters():
    result = terra.mint.parameters()
    print(result.get("mint_denom"))
    print(result.get("inflation_rate_change"))
    print(result.get("inflation_max"))
    print(result.get("inflation_min"))
    print(result.get("goal_bonded"))
    print(result.get("blocks_per_year"))
