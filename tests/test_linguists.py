import pytest

import numberize.linguists as linguists

EN_DATA = [
        ('twenty-five', 25), ('one', 1), ('hundred', 100),
        ('million', 1000000), ('billion', 1000000000), ('ruler', None),
        ('twenty-ten', None), ('one-two', None), ('two-three-four', None),
        ('yeay-sheeh', None), ('пять', None)
]


@pytest.mark.parametrize("token,expected_output", EN_DATA)
def test_en_linguist(token, expected_output):
    ling = linguists.EnLinguist()
    assert ling.get_number(token) == expected_output
