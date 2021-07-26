import pymorphy2

from my_types import Languages
from numeric_dict import nums


class Analyzer:
    def __init__(self, lang: Languages):
        self._morph = pymorphy2.MorphAnalyzer(lang=lang.name)

    def parse(self, word: str):
        return self._morph.parse(word)
