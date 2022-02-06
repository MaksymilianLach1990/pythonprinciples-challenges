import pytest

from type_check import onlyInts

sample_value_int = [
    (1, 2, True),
    (1, 'w', False),
    ('w', 't', False),
    (40, 34.9, False),
    (45, 90, True)
]

addition_names = (f"{value_1} and {value_2} are int? - {score}" for value_1, value_2, score in sample_value_int)

@pytest.mark.parametrize("value_1, value_2, score", sample_value_int, ids=addition_names)
def test_only_int(value_1, value_2, score):

    result = onlyInts(value_1, value_2)

    assert result == score
