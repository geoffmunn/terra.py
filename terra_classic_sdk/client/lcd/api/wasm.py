import base64
import json
from typing import Any, Union

from terra_classic_sdk.core import Numeric

from ._base import BaseAsyncAPI, sync_bind

__all__ = ["AsyncWasmAPI", "WasmAPI"]


class AsyncWasmAPI(BaseAsyncAPI):
    async def code_info(self, code_id: int) -> dict:
        """Fetches information about an uploaded code.

        Args:
            code_id (int): code ID

        Returns:
            dict: code information
        """
        res = await self._c._get(f"/cosmwasm/wasm/v1/code/{code_id}")
        code_info = res.get("code_info")
        return {
            "code_id": Numeric.parse(code_info["code_id"]),
            "data_hash": code_info["data_hash"],
            "creator": code_info["creator"],
        }

    async def contract_info(self, contract_address: str) -> dict:
        """Fetches information about an instantiated contract.

        Args:
            contract_address (str): contract address

        Returns:
            dict: contract information
        """
        res = await self._c._get(f"/cosmwasm/wasm/v1/contract/{contract_address}")
        
        contract_info = res.get("contract_info")
        
        if 'address' in contract_info:
            address = contract_info['address']
        else:
            address = ''

        if 'init_msg' in contract_info:
            init_msg = contract_info['init_msg']
        else:
            init_msg = ''

        return {
            "code_id": Numeric.parse(contract_info["code_id"]),
            "address": address,
            "creator": contract_info["creator"],
            "admin": contract_info.get("admin", None),
            "init_msg": init_msg
        }

    async def contract_query(self, contract_address: str, query: Union[dict, str]) -> Any:
        """Runs a QueryMsg on a contract.

        Args:
            contract_address (str): contract address
            query (dict): QueryMsg to run

        Returns:
            Any: results of query
        """
        
        params = base64.b64encode(json.dumps(query).encode("utf-8")).decode("utf-8")

        res = await self._c._get(
            f"/cosmwasm/wasm/v1/contract/{contract_address}/smart/{params}"
        )
        
        return res.get("data")
    
    async def parameters(self) -> dict:
        """Fetches the Wasm module parameters.

        @NOTE: BROKEN - DOES NOT RETURN EXPECTED RESULTS
        Returns:
            dict: Wasm module parameters
        """
        res = await self._c._get("/cosmwasm/wasm/v1/codes/params")
        params = res.get("params")
        return {
            "max_contract_size": Numeric.parse(params["max_contract_size"]),
            "max_contract_gas": Numeric.parse(params["max_contract_gas"]),
            "max_contract_msg_size": Numeric.parse(params["max_contract_msg_size"]),
        }


class WasmAPI(AsyncWasmAPI):
    @sync_bind(AsyncWasmAPI.code_info)
    def code_info(self, code_id: int) -> dict:
        pass

    code_info.__doc__ = AsyncWasmAPI.code_info.__doc__

    @sync_bind(AsyncWasmAPI.contract_info)
    def contract_info(self, contract_address: str) -> dict:
        pass

    contract_info.__doc__ = AsyncWasmAPI.contract_info.__doc__

    @sync_bind(AsyncWasmAPI.contract_query)
    def contract_query(self, contract_address: str, query: Union[dict, str]) -> Any:
        pass

    contract_query.__doc__ = AsyncWasmAPI.contract_query.__doc__

    @sync_bind(AsyncWasmAPI.parameters)
    def parameters(self) -> dict:
        pass

    parameters.__doc__ = AsyncWasmAPI.parameters.__doc__
