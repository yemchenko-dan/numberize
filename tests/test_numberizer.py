import pytest

import numberize.numberizer as numberizer

EN_DATA = [
    ("twenty-five", "25"),
    ("one hundred and nine", "100 and 9"),
    ("million dollars", "1000000 dollars"),
    ("There's a dog over the one's yard", "There's a dog over the 1's yard"),
    ("hundred", '100'),
    ("hundreds of thousands", "hundreds of thousands"),
    ("five-nine", "five-nine"),
    ("'two miLlion' - that's a number.", "'2000000' - that's a number."),
    (
        """
    Note the use of more than one conjunction "and" in large numbers in British
    English: two million six hundred and twenty-five thousand three hundred and
    ten (2,625,310).
    In American English, the conjunction "and" is generally not used before tens
    or ones: one hundred twenty-three (123);
    four hundred seven (407); three thousand five hundred thirty-eight (3,538);
    seventy-three thousand five (73,005);
    two million six hundred twenty-five thousand three hundred ten (2,625,310);
    five million three hundred thousand fifty (5,300,050).
    
    
    In British English, the conjunction "and" is also used before tens or ones
    in ordinal numerals above one hundred:
    one hundred and tenth (110th); three thousand and fifth (3005th).
    But "and" is not used in American ordinals:
    one hundred tenth (110th); three thousand fifth (3005th).
        """,
        """
    Note the use of more than 1 conjunction "and" in large numbers in British
    English: 2000600 and 25300 and
    10 (2,625,310).
    In American English, the conjunction "and" is generally not used before tens
    or ones: 123 (123);
    407 (407); 3538 (3,538);
    73005 (73,005);
    2625310 (2,625,310);
    5300050 (5,300,050).
    
    
    In British English, the conjunction "and" is also used before tens or ones
    in ordinal numerals above 100:
    100 and tenth (110th); 3000 and fifth (3005th).
    But "and" is not used in American ordinals:
    100 tenth (110th); 3000 fifth (3005th).
        """
    )
]

en_numberizer = numberizer.Numberizer('en')
ru_numberizer = numberizer.Numberizer('ru')
uk_numberizer = numberizer.Numberizer('uk')


@pytest.mark.parametrize("text,expected_output", EN_DATA)
def test_replace_numerals_en(text, expected_output):
    ans = ''.join(en_numberizer.replace_numerals(text).split())
    exp = ''.join(expected_output.split())
    assert ans == exp


# def test_replace_numerals_ru():
#     pass


# def test_replace_numerals_uk():
#     pass
