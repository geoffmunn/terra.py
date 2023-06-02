from terra_classic_sdk.client.lcd import LCDClient


def main():
    terra = LCDClient(
        url="https://terra-classic-lcd.publicnode.com",
        chain_id="columbus-5",
    )

    print(terra.tx.tx_infos_by_height(8152638))
    print(terra.tx.tx_infos_by_height(8153558))


main()
