from terra_classic_sdk.client.lcd import LCDClient, PaginationOptions

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)


def test_grants():
    result = terra.authz.grants(
        "terra1x46rqay4d3cssq8gxxvqz8xt6nwlz4td20k38v",
        "terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    )
    assert len(result) == 0
