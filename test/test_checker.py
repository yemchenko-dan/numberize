from numberize.analyze import Checker, Analyzer


def test_is_cyrillic_ru():
    char_bool = {
        'f': False,
        '.': False,
        'А': True,
        'в': True,
        'ї': False
    }
    checker = Checker('ru')
    for char in char_bool:
        ans = checker.is_cyrillic(char)
        assert ans == char_bool[char], char


def test_is_cyrillic_uk():
    char_bool = {
        'f': False,
        '.': False,
        'А': True,
        'в': True,
        'ї': True,
        "'": True
    }
    checker = Checker('uk')
    for char in char_bool:
        ans = checker.is_cyrillic(char)
        assert ans == char_bool[char], char


def test_get_parsed_ru():
    words = ('один', "сто", 'десять', 'тысяча')
    checker = Checker('ru')
    analyzer = Analyzer('ru')
    for word in words:
        assert checker.get_parsed(analyzer.parse(word))


def test_get_parsed_uk():
    words = ("один", "сто", "тисяча", "п'яти")
    checker = Checker('uk')
    analyzer = Analyzer('uk')
    for word in words:
        assert checker.get_parsed(analyzer.parse(word))
