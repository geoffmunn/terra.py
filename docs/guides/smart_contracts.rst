.. smart_contracts:

Working with Smart Contracts
============================

Contract Deployment Example
---------------------------

.. code-block:: python

    import base64
    from terra_classic_sdk.client.lcd.api.tx import CreateTxOptions
    from terra_classic_sdk.client.localterra import LocalTerra
    from terra_classic_sdk.core import Coins
    from terra_classic_sdk.core.wasm import MsgStoreCode, MsgInstantiateContract, MsgExecuteContract  
    from terra_classic_sdk.core.broadcast import BlockTxBroadcastResult
    from terra_classic_sdk.core.fee import Fee
    from terra_classic_sdk.core.wasm.data import AccessConfig

    terra = LocalTerra()
    test1 = terra.wallets["test1"]
    contract_file = open("./contract.wasm", "rb")

    permission:AccessConfig = AccessConfig(permission = 3, address = '')
    file_bytes = base64.b64encode(contract_file.read()).decode()
    store_code = MsgStoreCode(test1.key.acc_address, file_bytes, permission)
    store_code_tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[store_code],fee=Fee(2100000, "60000uluna")))
    store_code_tx_result = terra.tx.broadcast(store_code_tx)
    print(store_code_tx_result)

    code_id = store_code_tx_result.logs[0].events_by_type["store_code"]["code_id"][0]
    instantiate = MsgInstantiateContract(
        test1.key.acc_address,
        test1.key.acc_address,
        code_id,
        "Test",
        {"count": 0},
        {"uluna": 10000000}
    )
    instantiate_tx = test1.create_and_sign_tx(CreateTxOptions(msgs=[instantiate], fee=Fee(2100000, "60000uluna")))
    instantiate_tx_result:BlockTxBroadcastResult = terra.tx.broadcast(instantiate_tx)
    print(instantiate_tx_result)

    contract_address = instantiate_tx_result.logs[0].events_by_type[
        "instantiate"
    ]["_contract_address"][0]

    execute = MsgExecuteContract(
        test1.key.acc_address,
        contract_address,
        {"increment": {}},
        {"uluna": 100000},
    )

    execute_tx = test1.create_and_sign_tx(
        CreateTxOptions(msgs=[execute], fee=Fee(1000000, Coins(uluna=1000000)))
    )

    execute_tx_result = terra.tx.broadcast(execute_tx)
    print(execute_tx_result)

    result = terra.wasm.contract_query(contract_address, {"get_count": {}})
    print(result)
    
