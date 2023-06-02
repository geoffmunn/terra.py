from terra_classic_sdk.client.lcd import LCDClient

terra = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com")
res = terra.gov.deposits(proposal_id=5333)
print(res)
res = terra.gov.votes(proposal_id=5333)
print(res)
