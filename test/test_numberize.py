from dataclasses import dataclass

import numberize.numberize as nb


@dataclass
class QuestionMapAnswer:
    text: str
    map: list
    out: str


def test_replace_by_map():
    data_set = [
        QuestionMapAnswer('аодопддп', [('_', 0, 5)], '_ддп'),
        QuestionMapAnswer('аодопддп', [('_', 0, 5), (5, 6, 7)], '_д5п'),
    ]
    for item in data_set:
        ans = nb._replace_by_map(item.map, item.text)
        assert ans == item.out, ans


def test_replace_numerals_with_numbers():
    text_replaced = {
        'девять-восемь, тремя миллионами, шестьсот тысяч и трёх людей':
        '9-8, 3000000, 600000 и 3 людей',
        '"сто" - слово очень простое, состоит из трёх букв':
        '"100" - слово очень простое, состоит из 3 букв',

        'двадцать пять': '25',
        'двадцать пять и семь': '25 и 7',
        'двадцать пять тысяч и Вася': '25000 и Вася'
    }
    for text in text_replaced:
        ans = nb.replace_numerals_with_numbers(text)
        assert ans == text_replaced[text], ans
