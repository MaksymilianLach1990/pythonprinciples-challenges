import pytest

from capital_indexes import capitalIndexes

sample_words = [
    ('TEsT', [0,1,3]),
    ('pOżAR', [1,3,4]),
    ('OnOMatoPeJA', [0,2,3,7,9,10])
]

addition_names = (f"Word '{word}' - capital letter indexes {indexes}" 
                    for word, indexes in sample_words)

@pytest.mark.parametrize("word, score", sample_words, ids=addition_names)
def test_capital_indexes(word, score):

    result = capitalIndexes(word)

    assert result == score