import numberize

import numberize.analyze
import numberize.map_text


def test_get_replacement_map_ru():
    text_map = {
        'двадцать пять': [(25, 0, 13)],
        'восьмидесяти пяти и семи': [(85, 0, 17), (7, 20, 24)],
        'восьмидесяти пяти и семи .ю.карандашей': [(85, 0, 17), (7, 20, 24)],
        'восемь-девять, тремя миллионами гривен и "восемьюстами тысячами" ':
        [(8, 0, 6), (9, 7, 13), (3000000, 15, 31), (800000, 42, 63)]
    }
    analyzer = numberize.analyze.Analyzer('ru')
    checker = numberize.analyze.Checker('ru')
    mapper = numberize.map_text.Mapper(analyzer, checker)
    for text in text_map:
        ans = mapper.get_replacement_map(text)
        assert ans == text_map[text], ans



