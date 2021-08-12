from numberize import tokenizers
from numberize import replacers


class Numberizer:
    def __init__(self, lang: str = 'ru'):
        self.tokenizer = tokenizers.get_tokenizer(lang)
        self.replacer = replacers.get_replacer(lang)

    def replace_numerals(self, text: str) -> str:
        """Replaces numerals in text. Doesn't save indentation."""
        tokenized = self.tokenizer.tokenize(text)
        replaced = self.replacer.replace(tokenized)
        return self.tokenizer.detokenize(replaced)
