from terra_classic_sdk.client.lcd import LCDClient, PaginationOptions

terra = LCDClient(
    url="https://terra-classic-lcd.publicnode.com/",
    chain_id="columbus-5",
)

pagOpt = PaginationOptions(limit=2, count_total=True)


def test_proposals():
    result = terra.gov.proposals()
    assert result is not None


def test_proposals_with_pagination():
    result = terra.gov.proposals(PaginationOptions(limit=2))
    assert result is not None


def test_proposal():
    result = terra.gov.proposal(12073)
    assert result is not None


#public lcd requires tx.height
def test_proposer():
    result = terra.gov.proposer(12087)
    assert(result is not None)


#public lcd requires tx.height
def test_deposits():
   result = terra.gov.deposits(12073)
   assert(result is not None)


#public lcd requires tx.height
def test_deposits_with_pagination():
    result = terra.gov.deposits(12087, params=pagOpt)
    assert(result is not None)


#public lcd requires tx.height
def test_votes():
    result = terra.gov.votes(12073)
    assert(result is not None)


#public lcd requires tx.height
def test_votes_with_pagination():
    result = terra.gov.votes(12073, pagOpt)
    assert(result is not None)


def test_tally():
    result = terra.gov.tally(12073)
    assert result is not None


def test_deposit_parameters():
    result = terra.gov.deposit_parameters()
    assert result.get("min_deposit")
    assert result.get("max_deposit_period")


def test_voting_parameters():
    result = terra.gov.voting_parameters()
    assert result.get("voting_period")


def test_tally_parameters():
    result = terra.gov.tally_parameters()
    assert result.get("quorum")
    assert result.get("threshold")
    assert result.get("veto_threshold")


def test_parameters():
    result = terra.gov.parameters()
    assert result.get("deposit_params")
    assert result.get("voting_params")
    assert result.get("tally_params")
