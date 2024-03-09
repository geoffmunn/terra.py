from terra_classic_sdk.client.lcd import LCDClient
from terra_classic_sdk.client.lcd.params import PaginationOptions

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)
pagOpt = PaginationOptions(limit=1, count_total=True)


def test_delegations():
    result = terra.staking.delegations(
        validator="terravaloper17460j07rlktalgkll35zvz0efv60mv79m25hat",
        delegator=None,
        params=pagOpt,
    )
    assert result is not None
    result = terra.staking.delegations(
        validator=None,
        delegator="terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9",
        params=pagOpt,
    )
    assert result is not None
    result = terra.staking.delegations(
        validator="terravaloper17460j07rlktalgkll35zvz0efv60mv79m25hat",
        delegator="terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9",
    )
    assert result is not None
    result = terra.staking.delegation(
        validator="terravaloper17460j07rlktalgkll35zvz0efv60mv79m25hat",
        delegator="terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9",
    )
    assert result is not None


def test_unbonding():
    # result = terra.staking.unbonding_delegations(validator='terravaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                              delegator='terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp')
    # assert(result is not None)
    result = terra.staking.unbonding_delegations(
        validator="terravaloper17460j07rlktalgkll35zvz0efv60mv79m25hat", delegator=None
    )
    assert result is not None
    result = terra.staking.unbonding_delegations(
        validator=None,
        delegator="terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9",
        params=pagOpt,
    )
    assert result is not None
    # result = terra.staking.unbonding_delegation(validator='terravaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                             delegator='terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp')
    # assert(result is not None)


def test_validators():
    _pagOpt = PaginationOptions(limit=3, count_total=True, reverse=False)
    result = terra.staking.validators(_pagOpt)
    assert result is not None
    result = terra.staking.validator(
        "terravaloper17460j07rlktalgkll35zvz0efv60mv79m25hat"
    )
    assert result is not None


def test_redelagations():
    _pagOpt = PaginationOptions(limit=1, count_total=True, reverse=False)
    result = terra.staking.redelegations(
        "terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9", params=_pagOpt
    )
    assert result is not None
    # result = terra.staking.redelegations("terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    #                                      validator_src='terravaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                      params=_pagOpt)
    # assert(result is not None)
    # result = terra.staking.redelegations("terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    #                                      validator_dst='terravaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                      params=_pagOpt)
    # assert(result is not None)
    # result = terra.staking.redelegations("terra17lmam6zguazs5q5u6z5mmx76uj63gldnse2pdp",
    #                                      validator_src='terravaloper1vk20anceu6h9s00d27pjlvslz3avetkvnwmr35',
    #                                      validator_dst='terravaloper1ze5dxzs4zcm60tg48m9unp8eh7maerma38dl84')
    # assert(result is not None)


def test_bonded_validators():
    result = terra.staking.bonded_validators(
        "terra1em3qvwh0y6zd63pjmdppy3ztj0c6vyg6ek2rh9", pagOpt
    )
    assert result is not None


def test_pool():
    result = terra.staking.pool()
    assert result is not None


def test_parameters():
    result = terra.staking.parameters()
    assert result.get("unbonding_time")
    assert result.get("max_validators")
    assert result.get("max_entries")
    assert result.get("historical_entries")
    assert result.get("bond_denom")
