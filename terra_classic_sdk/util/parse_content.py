from typing import Union

from terra_classic_sdk.core.distribution.proposals import MsgCommunityPoolSpend
from terra_classic_sdk.core.gov.proposals import TextProposal
from terra_classic_sdk.core.params.proposals import ParameterChangeProposal
from terra_classic_sdk.core.ibc.proposals import ClientUpdateProposal
from terra_classic_sdk.core.wasm.proposals import MigrateContractProposal

from terra_classic_sdk.core.upgrade import (
    CancelSoftwareUpgradeProposal,
    SoftwareUpgradeProposal,
)
from terra_classic_sdk.core.wasm.proposals import UpdateAdminProposal

from terra_proto.cosmos.distribution.v1beta1 import MsgCommunityPoolSpend as MsgCommunityPoolSpend_pb
from terra_proto.cosmos.gov.v1beta1 import TextProposal as TextProposal_pb
from terra_proto.cosmos.params.v1beta1 import ParameterChangeProposal as ParameterChangeProposal_pb
from terra_proto.cosmos.upgrade.v1beta1 import (
    CancelSoftwareUpgradeProposal as CancelSoftwareUpgradeProposal_pb,
    SoftwareUpgradeProposal as SoftwareUpgradeProposal_pb
)
from terra_proto.ibc.core.client.v1 import ClientUpdateProposal as ClientUpdateProposal_pb

from .base import create_demux, create_demux_proto

Content = Union[
    TextProposal,
    MsgCommunityPoolSpend,
    ParameterChangeProposal,
    SoftwareUpgradeProposal,
    CancelSoftwareUpgradeProposal,
    ClientUpdateProposal,
    UpdateAdminProposal,
    MigrateContractProposal
]

parse_content = create_demux(
    [
        MsgCommunityPoolSpend,
        TextProposal,
        ParameterChangeProposal,
        SoftwareUpgradeProposal,
        CancelSoftwareUpgradeProposal,
        ClientUpdateProposal,
        UpdateAdminProposal,
        MigrateContractProposal
    ]
)

parse_content_proto = create_demux_proto(
    [
        MsgCommunityPoolSpend,
        TextProposal,
        ParameterChangeProposal,
        SoftwareUpgradeProposal,
        CancelSoftwareUpgradeProposal,
        ClientUpdateProposal,
        UpdateAdminProposal,
        MigrateContractProposal
    ]
)
"""
parse_content_proto = create_demux_proto(
    [
        [MsgCommunityPoolSpend.type_url, MsgCommunityPoolSpend_pb],
        [TextProposal.type_url, TextProposal_pb],
        [ParameterChangeProposal.type_url, ParameterChangeProposal_pb],
        [SoftwareUpgradeProposal.type_url, SoftwareUpgradeProposal_pb],
        [CancelSoftwareUpgradeProposal.type_url, CancelSoftwareUpgradeProposal_pb],
        [ClientUpdateProposal.type_url, ClientUpdateProposal_pb]
    ]
)
"""