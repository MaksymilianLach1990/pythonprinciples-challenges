import pytest

from divisible_by_3 import divisibleBy3

samble_number = [
    (3, True),
    (6, True),
    (7, False),
    (9, True),
    (3456, True)
]

@pytest.mark.parametrize("number, score", samble_number)
def test_divisible_by_3(number, score):

    result = divisibleBy3(number)

    assert result == score