LCDClient
=========

The :class:`LCDClient` is an object representing a HTTP connection to a Terra Classic LCD node.

Get connected
-------------

Create a new LCDClient instance by specifying the URL and chain ID of the node to connect to.

.. note::
    It is common practice to name the active LCDClient instance ``terra``, but this is not required.

.. code-block:: python

    >>> from terra_classic_sdk.client.lcd import LCDClient
    >>> terra = LCDClient(url="https://terra-classic-lcd.publicnode.com", chain_id="columbus-5")
    >>> terra.tendermint.node_info()['default_node_info']['network']

    'columbus-5'

You can also specify gas estimation parameters for your chain for building transactions.

.. code-block:: python

    >>> import requests
    >>> from terra_classic_sdk.client.lcd import LCDClient
    >>> from terra_classic_sdk.core import Coins

    >>> res = requests.get("https://terra-classic-fcd.publicnode.com/v1/txs/gas_prices")

    >>> terra = LCDClient(
            url="https://terra-classic-lcd.publicnode.com",
            chain_id="columbus-5",
            gas_prices=Coins(res.json()),
            gas_adjustment="1.4"
        ) 

    >>> terra.gas_prices

    Coins('0.95uaud,0.95ucad,0.7uchf,4.9ucny,4.5udkk,0.625ueur,0.55ugbp,5.85uhkd,10900.0uidr,54.4uinr,81.85ujpy,850.0ukrw,28.325uluna,2142.855umnt,3.0umyr,6.25unok,38.0uphp,0.52469usdr,6.25usek,1.0usgd,23.1uthb,20.0utwd,0.75uusd')

Using the module APIs
---------------------

LCDClient includes functions for interacting with each of the core modules (see sidebar). These functions are divided and
and organized by module name (eg. :class:`terra.market<terra_classic_sdk.client.lcd.api.market.MarketAPI>`), and handle 
the tedium of building HTTP requests, parsing the results, and handling errors. 

Each request fetches live data from the blockchain:

.. code-block:: python

    >>> from terra_classic_sdk.client.lcd import LCDClient
    >>> terra = LCDClient(url="https://terra-classic-lcd.publicnode.com", chain_id="columbus-5")
    >>> terra.market.parameters()
    
    {'base_pool': Dec('100000000000000'), 'pool_recovery_period': 18, 'min_stability_spread': Dec('1')}

The height of the last result (if applicable) is available:

.. code-block:: python

    >>> from terra_classic_sdk.client.lcd import LCDClient
    >>> terra = LCDClient(url="https://terra-classic-lcd.publicnode.com", chain_id="columbus-5")
    >>> terra.treasury.tax_rate()

    0.005000000000000000


Create a wallet
---------------

LCDClient can create a :class:`Wallet` object from any :class:`Key` implementation. Wallet objects
are useful for easily creating and signing transactions.

.. code-block:: python

    >>> import requests
    >>> from terra_classic_sdk.client.lcd import LCDClient
    >>> from terra_classic_sdk.client.lcd.wallet import Wallet
    >>> from terra_classic_sdk.core import Coins
    >>> from terra_classic_sdk.key.mnemonic import MnemonicKey

    >>> res = requests.get("https://terra-classic-fcd.publicnode.com/v1/txs/gas_prices")

    >>> mk = MnemonicKey(mnemonic='secret 24 word phrase')
    >>> terra = LCDClient(
        url="https://terra-classic-lcd.publicnode.com",
        chain_id="columbus-5",
        gas_prices=Coins(res.json()),
        gas_adjustment="1.4"
    )
    >>> wallet:Wallet = terra.wallet(mk)
    >>> wallet.account_number()

    5151262


LCDClient Reference
-------------------

.. autoclass:: terra_classic_sdk.client.lcd.LCDClient
    :members:
