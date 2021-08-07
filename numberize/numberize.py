import tokenize


class Numberizer:
    __supported = ('ru', 'uk', 'en')

    def __init__(self, lang: str = 'ru'):
        pass

    @classmethod
    def supported_languages(cls) -> tuple:
        return cls.__supported

    def replace_numerals(self, text: str) -> str:
        pass