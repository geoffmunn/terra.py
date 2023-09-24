from __future__ import annotations

from typing import Union

import attr

from terra_proto.osmosis.gamm.v1beta1 import PoolParams, PoolAsset
from terra_classic_sdk.util.json import JSONSerializable
from terra_classic_sdk.core import Numeric, Coin

@attr.s(frozen=True)
class Pool(JSONSerializable):
    """Represents a (denom, amount) pairing, analagous to ``sdk.Coin`` and ``sdk.DecCoin``
    in Cosmos SDK. Used for representing Terra native assets.
    """

    address: str                 = attr.ib()
    id: Numeric.Output           = attr.ib(converter = Numeric.parse)
    pool_params: PoolParams      = attr.ib()   
    future_pool_governor: str    = attr.ib()
    total_shares: Coin           = attr.ib()
    pool_assets: list            = attr.ib()
    total_weight: Numeric.Output = attr.ib(converter = Numeric.parse)

    # @staticmethod
    # def parse(arg: Union[Pool, str, dict]) -> Pool:
    #     """Converts the argument into a PoolParams object.

    #     Args:
    #         arg (Union[Coin, str, dict]): value to be converted to coin
    #     """
    #     if isinstance(arg, Pool):
    #         return arg
    #     elif isinstance(arg, str):
    #         return Pool.from_str(arg)
    #     else:
    #         return Pool.from_data(arg)

    # def to_amino(self) -> dict:
    #     return {"swap_fee": self.swap_fee, "exit_fee": self.exit_fee}

    def to_data(self) -> dict:

        pool_assets = []
        asset:PoolAsset
        for asset in self.pool_assets:
            pool_assets.append(asset.to_dict())

        result:dict = {
            'pool': {
                'address': self.address, 
                'future_pool_governor': self.future_pool_governor, 
                'id': self.id, 
                'pool_assets': pool_assets,
                'pool_params': self.pool_params.to_dict(),
                'total_weight': self.total_weight,
                'total_shares': self.total_shares.to_data()
            }
        }

        return result
    
    @classmethod
    def from_data(cls, data: dict) -> Pool:
        """Deserializes a :class:`Pool` object from its JSON data representation.

        Args:
            data (dict): data object
        """

        print ('data:', data)
        # Get the basic items
        address:str              = data['address']
        id:int                   = data['id']
        future_pool_governor:str = data['future_pool_governor']
        total_weight:str         = data['total_weight']

        # Construct the pool parameters
        pool_params:PoolParams = PoolParams().from_dict(data['pool_params'])

        # Shares are just Coin objects
        total_shares: Coin = Coin.from_data(data['total_shares'])
        
        # Build a list of assets
        pool_assets:list = []
        for asset in data['pool_assets']:
            pool_assets.append(PoolAsset().from_dict(asset))

        return cls(address, id, pool_params, future_pool_governor, total_shares, pool_assets, total_weight)