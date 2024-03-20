from typing import Optional

from ._base import BaseAsyncAPI, sync_bind

from terra_classic_sdk.client.lcd.params import PaginationOptions
from terra_classic_sdk.core.osmosis import Pool, PoolParams

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
    
    async def osmosis_pool_params(self, pool_id: int) -> Pool:
        """Fetches the pool parameter details based on the pool ID.
        This is specifically designed for Osmosis pools, and requires an Osmosis LCD to work.

        Args:
            pool_id (int): the pool id

        Returns:
            PoolParams: pool parameterinfo
        """

        res = await self._c._get(f"osmosis/gamm/v1beta1/pools/{pool_id}/params")

        # Load the result into a PoolParams object
        param_details:PoolParams = PoolParams.from_data(res['pool'])

        return param_details
    
    async def osmosis_pools(self) -> list:
        """Fetches all the available pools.
        This is specifically designed for Osmosis pools, and requires an Osmosis LCD to work.

        Args:
            None

        Returns:
            List: all available pools
        """
    
        pool_list:list = []

        # This is the default pagination object
        pagOpt:PaginationOptions = PaginationOptions(limit = 500, count_total = True)

        # Go and get the first batch of results
        res        = await self._c._get(f"osmosis/gamm/v1beta1/pools", params = pagOpt)
        pagination = res['pagination']
    
        # Load the result into a Pool object
        for item in res['pools']:
            pool_details:Pool = Pool.from_data(item)
            pool_list.append(pool_details)

        # Now keep doing this until we have no more paginated results
        while pagination['next_key'] is not None:
            pagOpt.key = pagination["next_key"]
            res        = await self._c._get(f"osmosis/gamm/v1beta1/pools", params = pagOpt)
            pagination = res['pagination']
            for item in res['pools']:
                pool_details:Pool = Pool.from_data(item)
                pool_list.append(pool_details)

        return pool_list

class PoolAPI(AsyncPoolAPI):
    @sync_bind(AsyncPoolAPI.osmosis_pool)
    def osmosis_pool(self, pool_id: int) -> Pool:
        pass

    osmosis_pool.__doc__ = AsyncPoolAPI.osmosis_pool.__doc__

    @sync_bind(AsyncPoolAPI.osmosis_pool_params)
    def osmosis_pool_params(self, pool_id: int) -> Pool:
        pass

    osmosis_pool_params.__doc__ = AsyncPoolAPI.osmosis_pool_params.__doc__

    @sync_bind(AsyncPoolAPI.osmosis_pools)
    def osmosis_pools(self) -> list:
        pass

    osmosis_pools.__doc__ = AsyncPoolAPI.osmosis_pools.__doc__
