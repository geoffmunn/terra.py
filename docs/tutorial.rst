.. quickstart:

Quickstart
==========


.. note:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Installation
------------

Terra Classic SDK can be installed (preferably in a :ref:`virtualenv <setup_environment>`)
using ``pip`` as follows:

.. code-block:: shell

   $ pip install -U terra-classic-sdk


.. note:: If you run into problems during installation, you might have a
    broken environment. See the troubleshooting guide to :ref:`setting up a
    clean environment <setup_environment>`.


Using Terra Classic SDK
---------------

In order to interact with the Terra Classic blockchain, you'll need a connection to a Terra Classic node.
This can be done through setting up an LCDClient:


.. code-block:: python

    from terra_classic_sdk.client.lcd import LCDClient

    terra = LCDClient(chain_id="columbus-5", url="https://terra-classic-lcd.publicnode.com")
    print(terra.tendermint.node_info())


Getting Blockchain Info
-----------------------

It's time to start using Terra Classic SDK! Once properly configured, the ``LCDClient`` instance will allow you
to interact with the Terra Classic blockchain. Try getting the latest block height:

.. code-block:: python

    >>> terra.tendermint.block_info()['block']['header']['height']
    '1687543'

Terra Classic SDK can help you read block data, sign and send transactions, deploy and interact with contracts,
and a number of other features.
