import pytest

from all_equal import allEqual, all_equal

sample_list = [
    ([1, 2, 3], False),
    ([1, 1, 1], True),
    ([2], True),
    ([0, 0, 0, 0], True)
]

@pytest.mark.parametrize("numbers, score", sample_list)
def test_all_Equal(numbers, score):

    result = allEqual(numbers)

    assert result == score

@pytest.mark.parametrize("numbers, score", sample_list)
def test_all_equal(numbers, score):

    result = all_equal(numbers)

    assert result == score