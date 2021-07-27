import pytest


import numberize
from numberize.analyze import Analyzer


def test__init__():
    with pytest.raises(ValueError):
        Analyzer('ku')
    for lang in numberize.Numberizer.supported_languages():
        assert Analyzer(lang), lang

