import numberize.map_text as map_text

from numberize.analyze import Analyzer, Checker


class Numberizer:
    _languages = ('ru', 'uk')

    def __init__(self, lang: str = 'ru'):
        """
        :param lang: 'ru' - russian, 'uk' - ukrainian
        """
        if lang in Numberizer._languages:
            self._analyzer = Analyzer(lang)
            self._checker = Checker(lang)
        else:
            raise Exception(
                f'{lang} is not supported language.\
                 Try one of these: {Numberizer._languages}'
            )

    @staticmethod
    def _replace_by_map(replacement_map, text) -> str:
        new_text = ''
        prev_end = 0
        for item in replacement_map:
            new_text += text[prev_end:item.start] + str(item.number)
            prev_end = item.end
        return new_text + text[prev_end:]

    def replace_numerals(self, text: str) -> str:
        mapper = map_text.Mapper(self._analyzer, self._checker)
        replacement_map = mapper.get_replacement_map(text)
        return self._replace_by_map(replacement_map, text)
