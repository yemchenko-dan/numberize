from abc import ABC, abstractmethod

from nltk.tokenize import word_tokenize


class Tokenizer(ABC):
    @staticmethod
    @abstractmethod
    def tokenize(text):
        """Splits sentences into words"""


class EnTokenizer(Tokenizer):
    @staticmethod
    def tokenize(text):
        return word_tokenize(text)


class RuTokenizer(Tokenizer):
    @staticmethod
    def tokenize(text):
        return word_tokenize(text, language='russian')


class UkTokenizer(Tokenizer):
    @staticmethod
    def _is_ukrainian(word: str) -> bool:
        allowed = {
            "а", "б", "в", "г", "д", "е", "є", "ж", "з", "і", "й", "к", "л",
            "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш",
            "щ", "ї", "ь", "я", "ю", "ж", "ґ", "-", "'", "’"
        }
        return set(word) <= allowed

    def _weld_apostrophes(self, tokens: list):
        new_tokens = []
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            if tok in ("’", "'") and i > 0 or i <= len(tok) - 1:
                prev_tok = tokens[i-1]
                next_tok = tokens[i+1]
                if self._is_ukrainian(prev_tok) \
                        and self._is_ukrainian(next_tok):
                    new_tokens += [''.join([prev_tok, tok, next_tok])]
                    i += 2
                    continue
            new_tokens += [tok]
            i += 1
        return new_tokens

    def tokenize(self, text):
        ru_tokenized = RuTokenizer.tokenize(text)
        return self._weld_apostrophes(ru_tokenized)


def get_tokenizer(lang: str):
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
