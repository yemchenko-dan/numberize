from time import perf_counter_ns

from numberize import tokenizers
from numberize import replacers

from numberize import texts


class Numberizer:
    def __init__(self, lang: str = 'ru'):
        self.tokenizer = tokenizers.get_tokenizer(lang)
        self.replacer = replacers.get_replacer(lang)

    def replace_numerals(self, text: str) -> str:
        tokenized = self.tokenizer.tokenize(text)
        replaced = self.replacer.replace(tokenized)
        return self.tokenizer.detokenize(tokenized)


tic = perf_counter_ns()

numba = Numberizer('uk')
print(
    numba.replace_numerals(texts.uk)
)
toc = perf_counter_ns()
print((toc-tic)/1E6)