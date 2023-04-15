Keys & Wallets
==============

A **Key** is an object that provides an abstraction for the agency of signing transactions.

Key (abstract)
--------------

Implementers of Keys meant for signing should override :meth:`Key.sign()<terra-classic_sdk.key.Key.sign>`
or :meth:`Key.create_signature()<terra-classic_sdk.key.key.Key.create_signature>` methods. More details are
available in :ref:`guides/custom_key`.

Some properties such as :meth:`acc_address<terra-classic_sdk.key.key.Key.acc_address>` and
:meth:`val_address<terra-classic_sdk.key.key.Key.val_address>` are provided.

.. automodule:: terra-classic_sdk.key.key
    :members:

RawKey
------

.. automodule:: terra-classic_sdk.key.raw
    :members:


MnemonicKey
-----------

.. automodule:: terra-classic_sdk.key.mnemonic
    :members:

Wallet
------

.. automodule:: terra-classic_sdk.client.lcd.wallet
    :members: