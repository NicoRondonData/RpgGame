import pytest

from app.talana_kombat_jrpg.fighters.arnaldor.main import Arnaldor
from app.talana_kombat_jrpg.fighters.tony.main import Tony


@pytest.fixture()
def tony():
    return Tony()


@pytest.fixture()
def arnaldor():
    return Arnaldor()
