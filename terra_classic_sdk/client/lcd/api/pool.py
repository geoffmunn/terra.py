from typing import Optional

from terra_classic_sdk.core import AccAddress, Coins

from ..params import APIParams
from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncPoolAPI", "PoolAPI"]


class AsyncPoolAPI(BaseAsyncAPI):
    #async def pool(self, pool_id: int) -> tuple(Coins, dict):
    async def osmosis_pool(self, pool_id: int):
        """Fetches the pool details based on the pool ID.
        This is specifically designed for Osmosis pools, and requires an Osmosis LCD to work.

        Args:
            pool_id (int): the pool id

        Returns:
            Coins: balance
            Pagination: pagination info
        """
        res = await self._c._get(f"osmosis/gamm/v1beta1/pools/{pool_id}")
        #return Coins.from_data(res["balances"]), res.get("pagination")
        return res

    # async def total(self, params: Optional[APIParams] = None) -> (Coins, dict):
    #     """Fetches the current total supply of all tokens.

    #     Returns:
    #         Coins: total supply
    #         params (APIParams, optional): additional params for the API like pagination
    #     """
    #     res = await self._c._get("/cosmos/bank/v1beta1/supply", params)
    #     return Coins.from_data(res.get("supply")), res.get("pagination")


class PoolAPI(AsyncPoolAPI):
    @sync_bind(AsyncPoolAPI.details)
    #def pool(self, pool_id: int) -> tuple(Coins, dict):
    def osmosis_pool(self, pool_id: int):
        pass

    osmosis_pool.__doc__ = AsyncPoolAPI.osmosis_pool.__doc__

    #@sync_bind(AsyncPoolAPI.total)
    #def total(self) -> (Coins, dict):
    #    pass

    #total.__doc__ = AsyncPoolAPI.total.__doc__
