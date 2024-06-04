"""Distribution module governance proposal types."""

from __future__ import annotations

import attr
from betterproto.lib.google.protobuf import Any as Any_pb
from terra_proto.cosmos.distribution.v1beta1 import (
    MsgCommunityPoolSpend as MsgCommunityPoolSpend_pb,
)

from terra_classic_sdk.core import AccAddress, Coins
from terra_classic_sdk.util.json import JSONSerializable

__all__ = ["MsgCommunityPoolSpend"]


@attr.s
class MsgCommunityPoolSpend(JSONSerializable):
    """Proposal for allocating funds from the community pool to an address.

    Args:
        title: proposal title
        description: proposal description
        recipient: designated recipient of funds if proposal passes
        amount (Coins): amount to spend from community pool
    """

    type_amino = "distribution/MsgCommunityPoolSpend"
    """"""
    type_url = "/cosmos.distribution.v1beta1.MsgCommunityPoolSpend"
    """"""
    prototype = MsgCommunityPoolSpend_pb
    """"""

    title: str = attr.ib()
    description: str = attr.ib()
    recipient: AccAddress = attr.ib()
    amount: Coins = attr.ib(converter=Coins)

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "title": self.title,
                "description": self.description,
                "recipient": self.recipient,
                "amount": self.amount.to_amino(),
            },
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgCommunityPoolSpend:
        return cls(
            title=data["title"],
            description=data["description"],
            recipient=data["recipient"],
            amount=Coins.from_data(data["amount"]),
        )

    def to_data(self) -> dict:
        return {
            "@type": self.type_url,
            "title": self.title,
            "description": self.description,
            "recipient": self.recipient,
            "amount": self.amount.to_data(),
        }

    def to_proto(self) -> MsgCommunityPoolSpend_pb:
        return MsgCommunityPoolSpend_pb(
            title=self.title,
            description=self.description,
            recipient=self.recipient,
            amount=self.amount.to_proto(),
        )

    @classmethod
    def from_proto(cls, proto: MsgCommunityPoolSpend_pb) -> MsgCommunityPoolSpend:
        return cls(
            title=proto.title,
            description=proto.description,
            recipient=proto.recipient,
            amount=Coins.from_proto(proto.amount),
        )

    def pack_any(self) -> Any_pb:
        return Any_pb(type_url=self.type_url, value=bytes(self.to_proto()))
