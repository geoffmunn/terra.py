Usage with Pagination
=====================

You can query information with Pagination to get information partially.

PaginationOption
----------------

.. autoclass:: terra_classic_sdk.client.lcd.params.APIParams
    :members:

.. autoclass:: terra_classic_sdk.client.lcd.params.PaginationOptions
    :members:

You can use PaginationOptions as APIParams for params of query functions.

.. code-block:: python

    from terra_classic_sdk.client.lcd import LCDClient, PaginationOptions

    terra = LCDClient(
        url="https://terra-classic-lcd.publicnode.com",
        chain_id="columbus-5"
    )

    result, pagination  = terra.gov.proposals()

    page_count:int = 1
    while pagination["next_key"] is not None:
        pagOpt = PaginationOptions(key=pagination["next_key"])
        proposals, pagination = terra.gov.proposals(params=pagOpt)
        pagOpt.key = pagination["next_key"]

        print ('****************')
        print (f'Page number {page_count}')
        for proposal in proposals:
            print (proposal.content.title)

        page_count += 1

