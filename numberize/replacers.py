from abc import ABC, abstractmethod

from pymorphy2 import MorphAnalyzer

from numberize.calculators import (
    Calculator, AmericanEnCalculator, CyrillicCalculator
)
from numberize.linguists import Linguist, EnLinguist, RuLinguist, UkLinguist


class Replacer(ABC):
    @abstractmethod
    def __init__(self, linguist: 'Linguist', calculator: 'Calculator'):
        """
        :param linguist: Linguist to convert numeral tokens to numbers
        :param calculator: Calculator to end result
        """

    @abstractmethod
    def calculate(self, numeral: tuple) -> str:
        """
        :param numeral: E.g. One hundred fifty-two is tuple(1, 100, 50, 2)
        :return: '152'
        """

    @abstractmethod
    def replace(self, tokens: list) -> list:
        """Replaces numerals in tokens by their numeric representation"""


class BasicReplacer(Replacer):
    def __init__(self, linguist: 'Linguist', calculator: 'Calculator'):
        self.linguist = linguist
        self.calculator = calculator

    def calculate(self, numeral: tuple) -> str:
        return self.calculator.calculate(numeral)

    def replace(self, tokens: list) -> list:
        new_tokens, current_numeral = [], ()
        for tok in tokens:
            number = self.linguist.get_number(tok)
            if number:
                current_numeral += (number, )
                continue
            if current_numeral:
                new_tokens += [self.calculate(current_numeral), tok]
                current_numeral = ()
                continue
            new_tokens += [tok]
        else:
            if current_numeral:
                new_tokens += [self.calculate(current_numeral)]
        return new_tokens


def get_replacer(lang: str) -> 'BasicReplacer':

    replacers = {
        'ru': BasicReplacer(
            RuLinguist(MorphAnalyzer(lang='ru', result_type=None)),
            CyrillicCalculator()
        ),
        'uk': BasicReplacer(
            UkLinguist(MorphAnalyzer(lang='uk', result_type=None)),
            CyrillicCalculator()
        ),
        'en': BasicReplacer(
            EnLinguist(),
            AmericanEnCalculator()
        )
    }

    if lang not in replacers:
        raise RuntimeError(
            f'Language is not supported. Use one of these: {replacers.keys()}'
        )
    return replacers[lang]
