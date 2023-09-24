from typing import Optional

#from terra_classic_sdk.core import AccAddress, Coins

from ..params import APIParams
from ._base import BaseAsyncAPI, sync_bind

from terra_classic_sdk.core.osmosis import Pool

__all__ = ["AsyncPoolAPI", "PoolAPI"]

class AsyncPoolAPI(BaseAsyncAPI):
    async def osmosis_pool(self, pool_id: int) -> Pool:
        """Fetches the pool details based on the pool ID.
        This is specifically designed for Osmosis pools, and requires an Osmosis LCD to work.

        Args:
            pool_id (int): the pool id

        Returns:
            Pool: pool info
        """

        res = await self._c._get(f"osmosis/gamm/v1beta1/pools/{pool_id}")

        # Load the result into a Pool object
        pool_details:Pool = Pool.from_data(res['pool'])

        return pool_details
    
    async def osmosis_pools(self) -> list:
        """Fetches all the available pools.
        This is specifically designed for Osmosis pools, and requires an Osmosis LCD to work.

        Args:
            None

        Returns:
            List: all available pools
        """

        res = await self._c._get(f"osmosis/gamm/v1beta1/pools")

        pool_list:list = []
        # Load the result into a Pool object
        for item in res['pools']:
            pool_details:Pool = Pool.from_data(item)
            pool_list.append(pool_details)

        return pool_list

    # async def total(self, params: Optional[APIParams] = None) -> (Coins, dict):
    #     """Fetches the current total supply of all tokens.

    #     Returns:
    #         Coins: total supply
    #         params (APIParams, optional): additional params for the API like pagination
    #     """
    #     res = await self._c._get("/cosmos/bank/v1beta1/supply", params)
    #     return Coins.from_data(res.get("supply")), res.get("pagination")

class PoolAPI(AsyncPoolAPI):
    @sync_bind(AsyncPoolAPI.osmosis_pool)
    def osmosis_pool(self, pool_id: int) -> Pool:
        pass

    osmosis_pool.__doc__ = AsyncPoolAPI.osmosis_pool.__doc__

    @sync_bind(AsyncPoolAPI.osmosis_pools)
    def osmosis_pools(self) -> list:
        pass

    osmosis_pools.__doc__ = AsyncPoolAPI.osmosis_pools.__doc__

    #@sync_bind(AsyncPoolAPI.total)
    #def total(self) -> (Coins, dict):
    #    pass

    #total.__doc__ = AsyncPoolAPI.total.__doc__
