import pymorphy2
from time import perf_counter_ns
from numberize.dawgs import uk_nums


def _bla(tok):
    morph = pymorphy2.MorphAnalyzer(lang='uk', result_type=None)
    for form in morph.normal_forms(tok):
        numb = uk_nums.get(form)
        if numb:
            return numb


tic = perf_counter_ns()
print(_bla("десятий"))
toc = perf_counter_ns()

print((toc - tic)/1E9)