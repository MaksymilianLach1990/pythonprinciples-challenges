import pytest

from counting_syllables import countingSyllables

sample_syllables = [
    ('syl-lab-es', 3),
    ('sam', 1),
    ('on-line', 2),
    ('asd-fgh-ert-qwe-rty', 5)
]

addition_names = (f"Word '{word}' have {number} syllables" for word, number  in sample_syllables)

@pytest.mark.parametrize("word, number", sample_syllables, ids=addition_names)
def test_counting_syllables(word, number):

    result = (countingSyllables(word))

    assert result == number