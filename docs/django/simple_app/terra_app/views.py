from django.http import HttpResponse
from terra_classic_sdk.client.lcd import LCDClient

# Create an instance of LCDClient to connect to the Terra Classic network
TERRA = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com")


def index(request):
    # This view returns an HTTP response
    # It displays information about the last block on the Terra Classic blockchain

    # Use the TERRA object to retrieve the latest block information
    block_height = TERRA.tendermint.block_info()['block']['header']['height']

    # Format the block height information into a string
    response_content = "Terra app, last block {} on Terra Classic blockchain.".format(block_height)

    # Return the formatted string as an HTTP response
    return HttpResponse(response_content)