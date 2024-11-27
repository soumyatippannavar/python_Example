import pytest


@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.other
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.parametrize("num, output",[(1,11),(4,44)])
def test_multiplication_11(num, output):
    assert 11*num == output


@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
