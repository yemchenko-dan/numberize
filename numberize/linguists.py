from abc import ABC, abstractmethod

import numberize.dawgs as dawgs


class Linguist(ABC):
    @staticmethod
    @abstractmethod
    def get_number(token: str):
        """
        E.g. 'two' -> 2, 'twenty-five' -> 25, "п'ять" -> 5, "миллион" -> 1E6
        'horse' -> None
        :param token: simple numeral
        :return: corresponding number, returns None if token is not a numeral
        """


class EnLinguist(Linguist):
    @staticmethod
    def get_number(token: str):
        if '-' in token:
            parts = token.split('-')
            if len(parts) != 2:
                return
            left = dawgs.en_nums.get(parts[0])
            if not left or left < 20 or left > 90:
                return
            right = dawgs.en_nums.get(parts[1])
            if not right or right > 9 or right < 1:
                return
            return left + right
        return dawgs.en_nums.get(token)


class RuLinguist(Linguist):
    def get_number(self, token: str):
        pass


class UkLinguist(Linguist):
    def get_number(self, token: str):
        pass
