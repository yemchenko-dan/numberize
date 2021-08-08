from abc import ABC, abstractmethod


class Replacer(ABC):
    @abstractmethod
    def __init__(self, linguist):
        """"""

    @staticmethod
    @abstractmethod
    def calculate(numeral: tuple) -> int:
        """
        :param numeral: E.g. One hundred fifty-two is tuple(1, 100, 50, 2)
        :return: 152
        """

    @abstractmethod
    def replace(self, tokens: list) -> list:
        """Replaces numerals in tokens by their numeric representation"""


class EnReplacer(Replacer):
    def __init__(self, linguist):
        self.linguist = linguist

    @staticmethod
    def calculate(numeral: tuple) -> int:
        pass

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


class RuReplacer(Replacer):
    pass


class UkReplacer(Replacer):
    pass


def get_replacer(lang):
    pass