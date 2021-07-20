import pymorphy2

import numberize as nb

morph = pymorphy2.MorphAnalyzer()


class Mapper:
    def __init__(self):
        self._replacement_map = []
        self._current_word = ''
        self._current_numeral = []
        self._start_of_numeral, self._end_of_numeral = None, None

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
            num_start = self._current_numeral[0][1]
            num_end = self._current_numeral[-1][2]
            num = nb.tools.calculate_a_num(
                (x[0] for x in self._current_numeral)
            )
            self._replacement_map.append((num, num_start, num_end))
            self._current_numeral = []

    def _update_numeral(self, end: int) -> None:
        self._end_of_numeral = end
        parsed = morph.parse(self._current_word)[0]
        if nb.tools.is_numeral(parsed.tag.POS, parsed.normal_form):
            self._current_numeral.append(
                (
                    nb.numeric_dict.all_num[parsed.normal_form],
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
            if nb.tools.is_cyrillic(char):
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
