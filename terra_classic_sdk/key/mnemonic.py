from __future__ import annotations

from bip32utils import BIP32_HARDEN, BIP32Key
from mnemonic import Mnemonic

from .raw import RawKey

__all__ = ["MnemonicKey"]

coin_types = {
    'cosmos': 118,
    'juno': 118,
    'kava': 459,
    'kujira': 118,
    'osmo': 118,
    'terra': 330,
    'emoney': 118,
    'sif': 118,
    'inj': 60,     # Possibly wrong coin type
    'axelar': 118,
    'umee': 118,
    'omniflix': 118,
    'gravity': 118,
    'somm': 118
}

class MnemonicKey(RawKey):
    """A MnemonicKey derives a private key using a BIP39 mnemonic seed phrase, and provides key-derivation options based on the BIP44 HD path standard.

    .. note:: You can change ``coin_type`` to 118 to derive the key for a legacy Terra
        wallet (shares ``coin_type`` with ATOM).

    Args:
        mnemonic (str, optional): space-separated mnemonic seed phrase. If not provided,
            a 24-word mnemonic will be generated.
        account (int, optional): HD path parameter - account number.
        index (int, optional): HD path parameter - account index.
        coin_type (int, optional): HD path parameter - coin type.
    """

    mnemonic: str
    """Mnemonic key phrase associated with the account (space-separated)."""

    account: int
    """HD path parameter: account number."""

    index: int
    """HD path parameter: account index."""

    coin_type: int
    """HD path parameter: coin type"""

    prefix: str
    """The prefix of the address - usually 'terra'"""

    @property
    def hd_path(self) -> str:
        """Returns the BIP32 HD path for key-derivation:

        ``m/44'/COIN_TYPE'/ACCOUNT'/0/INDEX'``

        Returns:
            str: full BIP32 HD path
        """
        return f"m/44'/{self.coin_type}'/{self.account}'/0/{self.index}"

    def __init__(
        self,
        mnemonic: str = None,
        account: int = 0,
        index: int = 0,
        prefix:str = 'terra'
    ):
        
        coin_type = coin_types[prefix]
        
        if mnemonic is None:
            mnemonic = Mnemonic("english").generate(256)
        seed = Mnemonic("english").to_seed(mnemonic)
        root = BIP32Key.fromEntropy(seed)
        # derive from hdpath
        child = (
            root.ChildKey(44 + BIP32_HARDEN)
            .ChildKey(coin_type + BIP32_HARDEN)
            .ChildKey(account + BIP32_HARDEN)
            .ChildKey(0)
            .ChildKey(index)
        )

        super().__init__(child.PrivateKey())
        self.mnemonic = mnemonic
        self.coin_type = coin_type
        self.account = account
        self.index = index
        self.address_prefix = prefix
