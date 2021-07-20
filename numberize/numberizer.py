import numberize.mapper as mp


def _replace_by_map(replacement_map: list, text: str) -> str:
    new_text = ''
    prev_end = 0
    for item in replacement_map:
        num, start, end = item
        new_text += text[prev_end:start] + str(num)
        prev_end = end
    return new_text + text[prev_end:]


def replace_numerals(text: str) -> str:
    mapper = mp.Mapper()
    replacement_map = mapper.get_replacement_map(text)
    return _replace_by_map(replacement_map, text)
