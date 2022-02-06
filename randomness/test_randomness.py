import pytest

from randomness import randomNumber

sample_range = [
    (1, 100),
    (2, 200),
    (0, 10),
    (1, 1000),
    (0, 15),
]

addition_names = (f"Random number from range from {min_value} to {max_value}" for min_value, max_value in sample_range)

@pytest.mark.parametrize("min_value, max_value", sample_range, ids=addition_names)
def test_random_number(min_value, max_value):

    for _ in range(20):

        result = randomNumber(min_value, max_value)

        assert min_value <= result
        assert max_value >= result