import pytest

from tic_tac_toe_input import ticTacToeInput

sample_fileds = [
    ('A1', (0, 0)),
    ('B1', (0, 1)),
    ('C3', (2, 2)),
    ('A2', (1, 0)),
    ('B3', (2, 1)),
]


@pytest.mark.parametrize('field, score', sample_fileds)
def test_tic_tac_toe_input(field, score):

    result = ticTacToeInput(field)

    assert result == score