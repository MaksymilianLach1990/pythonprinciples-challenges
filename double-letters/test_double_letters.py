import pytest

from double_letters import doubleLetters

sample_words = [
    ('hello', True),
    ('otto', True),
    ('mama', False),
    ('rewolwer', False),
    ('melon', False)
]

addition_names = (f"String {word} have double letter - {score}" for word, score in sample_words)

@pytest.mark.parametrize("word, score", sample_words, ids=addition_names)
def test_double_letter(word, score):

    result = doubleLetters(word)

    assert result == score