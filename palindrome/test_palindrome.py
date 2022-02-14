import pytest

from palindrome import palindrome

sample_words = [
    ('abba', True),
    ('word', False),
    ('asdfghjkl', False),
    ('asdfgfdsa', True)
]

@pytest.mark.parametrize("word, score", sample_words)
def test_palindrome(word, score):

    result = palindrome(word)

    assert result == score