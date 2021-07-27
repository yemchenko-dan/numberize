import numberize.tools as tools


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


def test_calculate_a_num():
    numbers_res = {
        (300, 80, 1): 381,
        (3, 1E6): 3000000,
        (5,): 5,
        (300, 60, 1E3, 80, 3): 360083
    }
    for numbers in numbers_res:
        ans = tools.calculate_a_num(numbers)
        assert ans == numbers_res[numbers], ans
