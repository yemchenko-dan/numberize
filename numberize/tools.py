import numberize.numeric_dict as nums


def is_cyrillic(char: str) -> bool:
    return char.lower() in 'абвгдеэёжзийклмнопрстуфхцшчщюяыьъ'


def is_numeral(part_of_speech: str, normal_form: str) -> bool:
    return part_of_speech == 'NUMR' or normal_form == 'сто'\
           or normal_form == 'один' or normal_form in nums.millenniums


def calculate_a_num(numbers) -> int:
    res, group = 0, 0
    for num in numbers:
        if num < 1E3:
            group += num
            continue
        if group != 0:
            res += group*num
            group = 0
            continue
        res += num
    else:
        res += group
    return int(res)
