import numberize.mapper as mp

from numberize.my_types import Languages
from numberize.analyze import Analyzer, Checker


class Numberizer:
    def __init__(self, lang: Languages = Languages.ru):
        self._analyzer = Analyzer(lang=lang)
        self._checker = Checker(lang=lang)

    @staticmethod
    def _replace_by_map(replacement_map, text) -> str:
        new_text = ''
        prev_end = 0
        for item in replacement_map:
            new_text += text[prev_end:item.start] + str(item.number)
            prev_end = item.end
        return new_text + text[prev_end:]

    def replace_numerals(self, text: str) -> str:
        mapper = mp.Mapper(self._analyzer, self._checker)
        replacement_map = mapper.get_replacement_map(text)
        return self._replace_by_map(replacement_map, text)
