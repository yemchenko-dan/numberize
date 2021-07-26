from enum import Enum
from collections import namedtuple


ReplacedNumeral = namedtuple('ReplacedNumeral', ['number', 'start', 'end'])


class Languages(Enum):
    ru = 'ru'
    uk = 'uk'