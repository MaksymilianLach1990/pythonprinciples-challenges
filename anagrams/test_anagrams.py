import pytest

from anagrams import isAnagram

sample_anagrams = [
    ('typhoon', 'opython', True),
    ('Alice', 'Bob', False),
    ('ab', 'ba', True),
    ('damaged', 'damag', False),
    ('work', 'working', False)
]

addition_names = (f"{word_1} and {word_2} are anagram? - {score}" for word_1, word_2, score in sample_anagrams)

@pytest.mark.parametrize('word_1, word_2, score', sample_anagrams, ids=addition_names)
def test_is_anagram(word_1, word_2, score):

    result = isAnagram(word_1, word_2)

    assert result == score
