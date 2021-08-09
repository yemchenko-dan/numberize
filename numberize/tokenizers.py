from abc import ABC, abstractmethod

from nltk.tokenize import word_tokenize, ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer


class Tokenizer(ABC):
    @staticmethod
    @abstractmethod
    def tokenize(text: str) -> list:
        """Splits sentences into words"""

    @staticmethod
    @abstractmethod
    def detokenize(tokens: list) -> str:
        """Joins tokens into text"""


class EnTokenizer(Tokenizer):
    @staticmethod
    def tokenize(text: str) -> list:
        return ToktokTokenizer().tokenize(text)

    @staticmethod
    def detokenize(tokens: list) -> str:
        return TreebankWordDetokenizer().detokenize(tokens)


class RuTokenizer(Tokenizer):
    @staticmethod
    def tokenize(text: str) -> list:
        return word_tokenize(text, language='russian')

    @staticmethod
    def detokenize(tokens: list) -> str:
        return TreebankWordDetokenizer().detokenize(tokens)


class UkTokenizer(Tokenizer):
    @staticmethod
    def _is_ukrainian(word: str) -> bool:
        allowed = {
            "а", "б", "в", "г", "д", "е", "є", "ж", "з", "і", "и", "й", "к",
            "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч",
            "ш", "щ", "ї", "ь", "я", "ю", "ж", "ґ", "-", "'", "’"
        }
        # TokTokTokenizer sometimes doesn't tokenize points in cyrillic text
        # E.g. ["дев", "'", "ятсот."]
        if word[-1] == '.' and len(word) > 3:
            word = word[:-1]
        return set(word) <= allowed

    def _weld_apostrophes(self, tokens: list) -> list:
        """Join words, that were split by apostrophes"""
        new_tokens = []
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok in ("’", "'") and 0 < i <= len(tokens) - 1:
                prev_tok = tokens[i-1]
                next_tok = tokens[i+1]
                if self._is_ukrainian(prev_tok) \
                        and self._is_ukrainian(next_tok):
                    new_tokens.pop()
                    new_tokens += [''.join([prev_tok, tok, next_tok])]
                    i += 2
                    continue
            new_tokens += [tok]
            i += 1
        return new_tokens

    def tokenize(self, text: str) -> list:
        ru_tokenized = ToktokTokenizer().tokenize(text)
        return self._weld_apostrophes(ru_tokenized)

    @staticmethod
    def detokenize(tokens: list) -> str:
        return TreebankWordDetokenizer().detokenize(tokens)


def get_tokenizer(lang: str) -> 'Tokenizer':
    """
    :param lang: available languages ('ru', 'uk', 'en')
    :return: Tokenizer object
    """
    tokenizers = {
        'ru': RuTokenizer(),
        'uk': UkTokenizer(),
        'en': EnTokenizer()
    }

    if lang not in tokenizers:
        raise RuntimeError(
            f'Language is not supported. Use one of these {tokenizers.keys()}'
        )
    return tokenizers[lang]
