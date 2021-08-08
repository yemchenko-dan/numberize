import numberize.linguists as linguists


def test_en_linguist():
    test_data = [
        ('twenty-five', 25), ('one', 1), ('hundred', 100),
        ('million', 1000000), ('billion', 1000000000), ('ruler', None),
        ('twenty-ten', None), ('one-two', None), ('two-three-four', None),
        ('yeay-sheeh', None), ('пять', None)
    ]
    ling = linguists.EnLinguist()
    for q_a in test_data:
        q, a = q_a
        assert a == ling.get_number(q)
