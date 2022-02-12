import pytest

from flatten import flattenList

sample_variable = [
    ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ([[9, 3, 5], [1]], [9, 3, 5, 1]),
    ([[2], [7, 8, 3]], [2, 7, 8, 3]),
    ([[56,83,67,43,56,23], [34,56,89,32]], [56,83,67,43,56,23,34,56,89,32])
]

@pytest.mark.parametrize('variables, score', sample_variable)
def test_flatten_list(variables, score):

    result = flattenList(variables)

    assert result == score