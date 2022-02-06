import pytest

from adding_removing_dots import addDots, removeDots

sample_words = [
    ('test', 't.e.s.t'),
    ('word', 'w.o.r.d'),
    ('elephant', 'e.l.e.p.h.a.n.t'),
    ('asdfghjkl', 'a.s.d.f.g.h.j.k.l')
]

addition_name = (f"{word} with dots - {word_dots}" for word, word_dots in sample_words)

@pytest.mark.parametrize("word, score", sample_words, ids=addition_name)
def test_add_dots(word, score):

    result = addDots(word)

    assert result == score

sample_words_dots = [
    ('t.e.s.t', 'test'),
    ('w.o.r.d', 'word'),
    ('e.l.e.p.h.a.n.t', 'elephant'),
    ('a.s.d.f.g.h.j.k.l', 'asdfghjkl')
]

addition_name = (f"{word_dots} without - {word}" for word_dots, word in sample_words_dots)

@pytest.mark.parametrize("word, score", sample_words_dots, ids=addition_name)
def test_remove_dots(word, score):

    result = removeDots(word)

    assert result == score
