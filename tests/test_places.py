import pytest
from rwanda.local import Places

NUMBER_OF_PROVINCES = 5
DISTRICT = 'Kigali'

@pytest.fixture
def validator():
    return Places()


def test_provinces(validator):
    """
    Test if provinces returns a list of provinces
    """
    assert len(validator.provinces()) == 5