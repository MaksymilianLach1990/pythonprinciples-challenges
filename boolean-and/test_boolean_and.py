import pytest

from boolean_and import tripleAnd, triple_and

sample_boolen = [
    (True, True, True, True),
    (False, False, False, False),
    (True, False, True, False),
    (True, False, False, False)
]

@pytest.mark.parametrize("var1, var2, var3, score", sample_boolen)
def test_triple_And(var1, var2, var3, score):

    result = tripleAnd(var1, var2, var3)

    assert result == score
    
@pytest.mark.parametrize("var1, var2, var3, score", sample_boolen)
def test_triple_and(var1, var2, var3, score):

    result = triple_and(var1, var2, var3)

    assert result == score
