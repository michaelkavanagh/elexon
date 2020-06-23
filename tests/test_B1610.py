import pytest
from elexon import ElexonRawClient


def read_key_from_file(filename='../elexon_key.txt'):
    with open(filename, "r") as key_file:
        key = key_file.read()
    return key


def test_B1610_period_exists():
    key = read_key_from_file()
    api = ElexonRawClient(key, 'v2')
    generation = api.Transparency.B1610(SettlementDate='2020-01-01', Period='2', NGCBMUnitID='CAS-BEU01')
    assert generation[0]['Period']


if __name__ == "__main__":
    pytest.main()
    #test_B1610_period_exists()