def test_is_cyrillic():
    char_bool = {
        'f': False,
        '.': False,
        'А': True,
        'в': True
    }
    for char in char_bool:
        ans = tools.is_cyrillic(char)
        assert ans == char_bool[char], ans


def test_is_numeral():
    pair_bool = {
        ('NUMR', 'fga'): True,
        ('ADJV', 'один'): True,
        ('NOUN', 'сто'): True,
        ('PROV', 'тысяча'): True,
        ('GGG', 'gasg'): False
    }
    for pair in pair_bool:
        pos, normal_form = pair
        ans = tools.is_numeral(pos, normal_form)
        assert ans == pair_bool[pair], ans
