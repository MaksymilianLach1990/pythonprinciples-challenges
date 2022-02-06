import pytest

from middle_letter import middleLetter

sample_string = [
    ('asd', 's'),
    ('psrt', ''),
    ('asdadsdfg', 'd'),
    ('asdaaaaaaayddddddddda', 'y'),
    ('alrychstebgizkapedft', '')
]

addition_names = (f"In '{string}' - middle letter is '{letter}'" for string, letter in sample_string)

@pytest.mark.parametrize('string, letter', sample_string, ids=addition_names)
def test_middle_letter(string, letter):

    result = middleLetter(string)

    assert result == letter