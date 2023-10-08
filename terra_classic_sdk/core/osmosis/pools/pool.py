from __future__ import annotations

import attr

from terra_proto.osmosis.gamm.v1beta1 import PoolParams, PoolAsset
from terra_classic_sdk.util.json import JSONSerializable
from terra_classic_sdk.core import Numeric, Coin

@attr.s(frozen=True)
class Pool(JSONSerializable):
    """Represents a (denom, amount) pairing, analagous to ``sdk.Coin`` and ``sdk.DecCoin``
    in Cosmos SDK. Used for representing Terra native assets.
    """

    type: str                    = attr.ib()
    address: str                 = attr.ib()
    id: Numeric.Output           = attr.ib(converter = Numeric.parse)
    pool_params: PoolParams      = attr.ib()   
    future_pool_governor: str    = attr.ib()
    total_shares: Coin           = attr.ib()
    pool_assets: list            = attr.ib()
    total_weight: Numeric.Output = attr.ib(converter = Numeric.parse)

    def to_data(self) -> dict:

        pool_assets = []
        asset:PoolAsset
        for asset in self.pool_assets:
            pool_assets.append(asset.to_dict())

        result:dict = {
            'pool': {
                'type': self.type,
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

        # Get the basic items
        type:str    = data['@type']
        address:str = data['address']
        id:int      = data['id']
        
        if 'future_pool_governor' in data:
            future_pool_governor:str = data['future_pool_governor']
        else:
            future_pool_governor:str = ''

        if 'total_weight' in data:
            total_weight:int = data['total_weight']
        else:
            total_weight:int = 0

        # Construct the pool parameters
        if 'pool_params' in data:
            pool_params:dict = data['pool_params']
        else:
            pool_params:dict = {'swap_fee': 0, 'exit_fee': 0, 'smooth_weight_change_params': None, 'spread_factor': data['spread_factor']}

        pool_params:PoolParams = PoolParams().from_dict(pool_params)

        # Shares are just Coin objects
        if 'total_shares' in data:
            total_shares: Coin = Coin.from_data(data['total_shares'])
        else:
            total_shares: Coin = None
        
        # Build a list of assets
        pool_assets:list = []
        #/osmosis.concentratedliquidity.v1beta1.Pool
        #/osmosis.gamm.v1beta1.Pool
        if type != '/osmosis.gamm.poolmodels.stableswap.v1beta1.Pool':
            if 'pool_assets' in data:
                for asset in data['pool_assets']:
                    pool_assets.append(PoolAsset().from_dict(asset))
            else:
                for asset in ['token0', 'token1']:
                    pool_assets.append(PoolAsset().from_dict({
                        "token": {
                            "denom": data[asset],
                            "amount": 0
                        },
                        "weight": 0
                    }))
        
        return cls(type, address, id, pool_params, future_pool_governor, total_shares, pool_assets, total_weight)