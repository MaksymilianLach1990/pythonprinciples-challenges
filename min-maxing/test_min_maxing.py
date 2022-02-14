import pytest

from min_maxing import minMaxing
sample_numbers = [
    ([1, 2, 3], 2),
    ([-100, 0, 100], 200),
    ([-345, -45, 235, 598, 248], 943)
]

@pytest.mark.parametrize("numbers, score", sample_numbers)
def test_min_maxing(numbers, score):

    result = minMaxing(numbers)

    assert result == score