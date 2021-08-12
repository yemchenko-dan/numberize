from abc import ABC, abstractmethod


class Calculator(ABC):
    @staticmethod
    @abstractmethod
    def calculate(numeral: tuple) -> str:
        """
        :param numeral: E.g. One hundred fifty-two is tuple(1, 100, 52)
        :return: '152'
        """


class AmericanEnCalculator(Calculator):
    @staticmethod
    def calculate(numeral: tuple) -> str:
        res, h_group, m_group = 0, 0, 0
        for num in numeral:
            if num == 100:
                if h_group != 0:
                    m_group += h_group * num
                    h_group = 0
                    continue
                m_group += num
                continue
            if num >= 1000:
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
        return str(int(res))


class CyrillicCalculator(Calculator):
    @staticmethod
    def calculate(numeral: tuple) -> str:
        res, group = 0, 0
        for num in numeral:
            if num < 1E3:
                group += num
                continue
            if group != 0:
                res += group * num
                group = 0
                continue
            res += num
        else:
            res += group
        return str(int(res))
