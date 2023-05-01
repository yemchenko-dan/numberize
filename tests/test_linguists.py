import pytest

import pymorphy3

import numberize.linguists as linguists

EN_DATA = [
        ("twenty-five", 25), ("one", 1), ("hundred", 100),
        ("million", 1000000), ("billion", 1000000000), ("ruler", None),
        ("twenty-ten", None), ("one-two", None), ("two-three-four", None),
        ("yeay-sheeh", None), ("пять", None)
]

RU_DATA = [
    ("пять", 5), ("five", None), ("ста", 100), ("одного", 1),
    ("тысячи", 1000), ("сто", 100), ("п'яти", None), ("дваДцати.", 20)
]

UK_DATA = [
    ("п'яти.", 5), ("ста", 100), ("five", None), ("пяти", None),
    ("сімох", 7), ("ТисЯчі", 1000), ("Ти сячі", None),
    ("мільйона", 1000000)
]

ru_morph = pymorphy3.MorphAnalyzer(result_type=None)
uk_morph = pymorphy3.MorphAnalyzer(lang="uk", result_type=None)


@pytest.mark.parametrize("token,expected_output", EN_DATA)
def test_en_linguist(token, expected_output):
    ling = linguists.EnLinguist()
    assert ling.get_number(token) == expected_output


@pytest.mark.parametrize("token,expected_output", RU_DATA)
def test_ru_linguist(token, expected_output):
    ling = linguists.RuLinguist(ru_morph)
    assert ling.get_number(token) == expected_output


@pytest.mark.parametrize("token,expected_output", UK_DATA)
def test_uk_linguist(token, expected_output):
    ling = linguists.UkLinguist(uk_morph)
    assert ling.get_number(token) == expected_output
