from numberize.analyze import Analyzer, Checker
from numberize.my_types import ReplacedNumeral


def calculate_a_num(numbers) -> int:
    res, group = 0, 0
    for num in numbers:
        if num < 1E3:
            group += num
            continue
        if group != 0:
            res += group*num
            group = 0
            continue
        res += num
    else:
        res += group
    return int(res)


class Mapper:
    def __init__(self, analyzer: 'Analyzer', checker: 'Checker'):
        self._replacement_map = []
        self._current_word = ''
        self._current_numeral = []
        self._start_of_numeral, self._end_of_numeral = None, None

        self._morph = analyzer
        self._check = checker

    def _clear(self):
        self._replacement_map = []
        self._current_word = ''
        self._current_numeral = []
        self._start_of_numeral, self._end_of_numeral = None, None

    def _update_word(self, char: str, start: int) -> None:
        if not self._current_word:
            self._start_of_numeral = start
        self._current_word += char

    def _update_replacement_map(self) -> None:
        if self._current_numeral:
            num_start = self._current_numeral[0].start
            num_end = self._current_numeral[-1].end
            num = calculate_a_num(
                (x.number for x in self._current_numeral)
            )
            self._replacement_map.append(
                ReplacedNumeral(num, num_start, num_end)
            )
            self._current_numeral = []

    def _update_numeral(self, end: int) -> None:
        self._end_of_numeral = end
        parsed = self._check.get_parsed(self._morph.parse(self._current_word))
        if parsed:
            self._current_numeral.append(
                ReplacedNumeral(
                    self._check.get_num(parsed.normal_form),
                    self._start_of_numeral,
                    self._end_of_numeral
                )
            )
        else:
            self._update_replacement_map()
        self._current_word = ''

    def get_replacement_map(self, text: str) -> list:
        self._clear()
        for current_position, char in enumerate(text):
            if self._check.is_cyrillic(char):
                self._update_word(char, start=current_position)
            elif self._current_word:
                if char.isspace():
                    self._update_numeral(end=current_position)
                    continue
                self._update_numeral(end=current_position)
                self._update_replacement_map()
            elif not char.isspace():
                self._update_replacement_map()
        else:
            if self._current_word:
                self._update_numeral(end=len(text))
                self._update_replacement_map()
            if self._current_numeral:
                self._update_replacement_map()
        return self._replacement_map

