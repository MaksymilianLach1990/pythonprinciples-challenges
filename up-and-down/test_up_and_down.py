import pytest

from up_and_down import upAndDown

sample_numbers = [
    (1, (0, 2)),
    (34, (33, 35)),
    (3456, (3455, 3457))
]

@pytest.mark.parametrize("number, score", sample_numbers)
def test_up_and_down(number, score):

    result = upAndDown(number)

    assert result == score