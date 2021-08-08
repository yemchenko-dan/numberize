from abc import ABC, abstractmethod

import dawgs


class Linguist(ABC):
    @abstractmethod
    def get_number(self, token: str):
        """
        E.g. 'two' -> 2, 'twenty-five' -> 25, "п'ять" -> 5, "миллион" -> 1E6
        'horse' -> None
        :param token: simple numeral
        :return: corresponding number, returns None if token is not a numeral
        """


class EnLinguist(Linguist):
    def get_number(self, token: str):
        if '-' in token:
            parts = token.split('-')
            if len(parts) != 2:
                return
            left = dawgs.en_nums.get(parts[0])
            right = dawgs.en_nums.get(parts[1])
            return left + right if left and right else None
        return dawgs.en_nums.get(token)


class RuLinguist(Linguist):
    def get_number(self, token: str):
        pass


class UkLinguist(Linguist):
    def get_number(self, token: str):
        pass
