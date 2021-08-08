from abc import ABC, abstractmethod

from numberize.linguists import EnLinguist, RuLinguist, UkLinguist


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
        res, h_group, m_group = 0, 0, 0
        for num in numeral:
            if num == 100:
                if h_group != 0:
                    m_group += h_group * num
                    h_group = 0
                    continue
                m_group += num
            if num in (1000, 1000000, 1000000000):
                if h_group and m_group:
                    res += (h_group + m_group) * num
                    h_group, m_group = 0, 0
                elif h_group:
                    res += h_group * num
                    h_group = 0
                elif m_group:
                    res += m_group * num
                    m_group = 0
                else:
                    res += num
                continue
            h_group += num
        else:
            res += m_group + h_group
        return int(res)

    def replace(self, tokens: list) -> list:
        new_tokens, current_numeral = [], ()
        for tok in tokens:
            number = self.linguist.get_number(tok)
            if number:
                current_numeral += (number, )
                continue
            if current_numeral:
                new_tokens += [str(self.calculate(current_numeral)), tok]
                current_numeral = ()
                continue
            new_tokens += [tok]
        else:
            if current_numeral:
                new_tokens += [str(self.calculate(current_numeral))]
        return new_tokens


class RuReplacer(Replacer):
    pass


class UkReplacer(Replacer):
    pass


def get_replacer(lang):

    replacers = {
        'ru': RuReplacer,
        'uk': UkReplacer,
        'en': EnReplacer(EnLinguist)
    }

    if lang not in replacers:
        raise RuntimeError(
            f'Language is not supported. Use one of these: {replacers.keys()}'
        )
    return replacers[lang]
