import pytest

from consecutive_zeros import consecutiveZeros, countZero

sample_numbers = [
    ('010101010110', 1),
    ('11000111000100', 3),
    ('01101100111', 2),
    ('01', 1),
    ('10000001', 6)
]

@pytest.mark.parametrize('number, score', sample_numbers)
def test_count_zero(number, score):

    result = countZero(number)

    assert result == score

@pytest.mark.parametrize('number, score', sample_numbers)
def test_consecutive_zeros(number, score):

    result = consecutiveZeros(number)

    assert result == score