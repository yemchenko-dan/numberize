import pytest

from numberize.calculators import AmericanEnCalculator, CyrillicCalculator

EN_DATA = [
    ((100, ), '100'),
    ((25, ), '25'),
    ((1, ), '1'),
    ((1000, ), '1000'),
    ((99, ), '99'),
    ((1000000, ), '1000000'),
    ((1, 100, 25), '125'),
    ((1, 100), '100'),
    ((2, 1000000, 6, 100, 25, 1000, 3, 100, 10), '2625310')
]

CYRILLIC_DATA = [
    ((1, ), '1'),
    ((10, ), '10'),
    ((100, ), '100'),
    ((1000, ), '1000'),
    ((20, 5), '25'),
    ((100, 20, 5), '125'),
    ((6, 1000000, 600, 5, 1000, 20), '6605020'),
    ((1000000, ), '1000000')
]


@pytest.mark.parametrize("numeral,expected_output", EN_DATA)
def test_american_en_calculator(numeral, expected_output):
    assert AmericanEnCalculator().calculate(numeral) == expected_output


@pytest.mark.parametrize("numeral,expected_output", CYRILLIC_DATA)
def test_cyrillic_calculator(numeral, expected_output):
    assert CyrillicCalculator().calculate(numeral) == expected_output
