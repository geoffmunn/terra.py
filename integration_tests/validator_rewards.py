from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com")
print(
    terra.distribution.validator_rewards(
        "terravaloper1259cmu5zyklsdkmgstxhwqpe0utfe5hhyty0at"
    )
)
