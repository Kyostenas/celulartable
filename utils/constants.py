from typing import NamedTuple
from utils.micro_classes import (
    Empty
)


class TypeNames(NamedTuple):
    bool_: str
    str_: str
    int_: str
    float_: str
    bytes_: str
    none_type_: str
    empty: str


class ColumnAligns(NamedTuple):
    left: str
    right: str
    center: str
    float_: str
    bytes_: str


# (o==================================================================o)
#   CELL SECTION (START)
#   constants created for the Cell class.
# (o-----------------------------------------------------------\/-----o)

DEFAULT_STYLE_NAME = 'grid'
DEFAULT_MISSING_VALUE = ''
DEFAULT_CELL_ALIGNMENT = 'l'

BOLD_WIDTH_NAME = 'bold'
THIN_WIDTH_NAME = 'thin'
ACCEPTED_WIDTHS = {
    BOLD_WIDTH_NAME: True,
    THIN_WIDTH_NAME: False
}
DEFAULT_BORDER_WIDTH = ACCEPTED_WIDTHS[THIN_WIDTH_NAME]

CENTERED = '^'
RIGHT_ALIGNED = '>'
LEFT_ALIGNED = '<'
TO_RIGHT_ALIGN = ['r', 'f']
TO_CENTER = ['c']

COLUMN_ALIGNS = ColumnAligns(
    left='l',
    right='r',
    center='c',
    float_='f',
    bytes_='b',
)
ALIGNMENTS = {
    COLUMN_ALIGNS.left : 'left',
    COLUMN_ALIGNS.right : 'right',
    COLUMN_ALIGNS.center : 'center',
    COLUMN_ALIGNS.float_ : 'float',
    COLUMN_ALIGNS.bytes_ : 'bytes',
}

# (o-----------------------------------------------------------/\-----o)
#   CELL SECTION (END)
# (o==================================================================o)


# (o==================================================================o)
#   CELULARTABLE SECTION (START)
#   constants created for the CelularTable class
# (o-----------------------------------------------------------\/-----o)

UPPER_LOWER_CELL_ROW_HEIGHT = 2
PENULT_CELL_ROW_HEIGHT = 3

FIRST = 0
PENULT = -2
LAST = -1
AT_LEAST_ONE = 0
AT_LEAST_TWO = 1
AT_LEAST_THREE = 2
AT_LEAST_FOUR = 3
SECOND_TO_ANTE_PENULT = slice(1, -2)

DEFAULT_MISSING_VALUE = ''

TYPE_NAMES = TypeNames(
    bool_=bool.__name__,
    str_=str.__name__,
    int_=int.__name__,
    float_=float.__name__,
    bytes_=bytes.__name__,
    none_type_=type(None).__name__,
    empty=Empty.__name__,
)
ALIGNMENTS_PER_TYPE = {
    TYPE_NAMES.bool_: COLUMN_ALIGNS.right,
    TYPE_NAMES.str_: COLUMN_ALIGNS.left,
    TYPE_NAMES.int_: COLUMN_ALIGNS.right,
    TYPE_NAMES.float_: COLUMN_ALIGNS.float_,
    TYPE_NAMES.bytes_: COLUMN_ALIGNS.bytes_,
    TYPE_NAMES.none_type_: COLUMN_ALIGNS.left,
}
CAN_WRAP_TYPES = [
    TYPE_NAMES.str_,
    TYPE_NAMES.none_type_,
]

# (o-----------------------------------------------------------/\-----o)
#   CELULARTABLE SECTION (END)
# (o==================================================================o)