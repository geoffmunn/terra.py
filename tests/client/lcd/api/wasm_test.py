from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)


def test_code_info():
    result = terra.wasm.code_info(3)
    assert result is not None


def test_contract_info():
    result = terra.wasm.contract_info("terra1vrqd7fkchyc7wjumn8fxly88z7kath4djjls3yc5th5g76f3543salu48s")
    assert result is not None


def test_contract_query():
    result = terra.wasm.contract_query(
        "terra1vrqd7fkchyc7wjumn8fxly88z7kath4djjls3yc5th5g76f3543salu48s",
        {"config": {}},
    )
    assert result is not None


# Does not currently return the expected results
# def test_parameters():
#     result = terra.wasm.parameters()
#     assert result.get("max_contract_size")
#     assert result.get("max_contract_gas")
#     assert result.get("max_contract_msg_size")
