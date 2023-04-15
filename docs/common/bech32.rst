.. bech32:

Bech32 Strings
==============

To provide some clarity for arguments, some functions in the SDK are documented that
they take a type like :class:`AccAddress` where one may expect a ``str``. It is simply a
type alias annotation (equivalent to ``str``) that serves only to remind the developer
which format the string is expected to be in. 

Terra SDK also provides useful functions for checking and converting **addresses** and **pubkeys**.

Addresses
---------

AccAddress
^^^^^^^^^^

.. autoclass:: terra-classic_sdk.core.bech32.AccAddress
    :members:

.. autofunction:: terra-classic_sdk.core.bech32.is_acc_address

.. autofunction:: terra-classic_sdk.core.bech32.to_acc_address

ValAddress
^^^^^^^^^^

.. autoclass:: terra-classic_sdk.core.bech32.ValAddress
    :members:

.. autofunction:: terra-classic_sdk.core.bech32.is_val_address

.. autofunction:: terra-classic_sdk.core.bech32.to_val_address



PubKeys
-------

AccPubKey
^^^^^^^^^

.. autoclass:: terra-classic_sdk.core.bech32.AccPubKey
    :members:

.. autofunction:: terra-classic_sdk.core.bech32.is_acc_pubkey

.. autofunction:: terra-classic_sdk.core.bech32.to_acc_pubkey

ValPubKey
^^^^^^^^^

.. autoclass:: terra-classic_sdk.core.bech32.ValPubKey
    :members:

.. autofunction:: terra-classic_sdk.core.bech32.is_acc_pubkey

.. autofunction:: terra-classic_sdk.core.bech32.to_acc_pubkey

