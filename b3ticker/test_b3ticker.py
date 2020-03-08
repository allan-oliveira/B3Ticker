import pytest
from b3ticker.b3ticker import B3Ticker

def test_default_initial_amount():
    b3ticker = B3Ticker()
    cvm_codes = b3ticker.get_cvm_codes(set('A'))
    assert not len(cvm_codes) == 0