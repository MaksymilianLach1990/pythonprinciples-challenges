import pytest

from custom_zip import customZip

sample_list = [
    ([1, 2, 3], [2, 3, 4], [(1, 2), (2, 3), (3, 4)]),
    ([3, 2, 1], [9, 8, 7], [(3, 9), (2, 8), (1, 7)])
]

@pytest.mark.parametrize("list1, list2, score", sample_list)
def test_custom_zip(list1, list2, score):

    result = customZip(list1, list2)

    assert result == score