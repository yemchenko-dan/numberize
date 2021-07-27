from dataclasses import dataclass

from numberize import Numberizer
from numberize.my_types import ReplacedNumeral


@dataclass
class QuestionMapAnswer:
    text: str
    map: list
    out: str


def test_replace_by_map():
    data_set = [
        QuestionMapAnswer(
            'аодопддп', [ReplacedNumeral('_', 0, 5)], '_ддп'
        ),
        QuestionMapAnswer(
            'аодопддп',
            [ReplacedNumeral('_', 0, 5), ReplacedNumeral(5, 6, 7)],
            '_д5п'
        ),
    ]
    numba = Numberizer('ru')
    for item in data_set:
        ans = numba._replace_by_map(item.map, item.text)
        assert ans == item.out, ans


def test_replace_numerals_ru():
    text_replaced = {
        'девять-восемь, тремя миллионами, шестьсот тысяч и трёх людей':
        '9-8, 3000000, 600000 и 3 людей',
        '"сто" - слово очень простое, состоит из трёх букв':
        '"100" - слово очень простое, состоит из 3 букв',

        'двадцать пять': '25',
        'двадцать пять и семь': '25 и 7',
        'двадцать пять тысяч и Вася': '25000 и Вася'
    }
    numba = Numberizer('ru')
    for text in text_replaced:
        ans = numba.replace_numerals(text)
        assert ans == text_replaced[text], ans

