

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

ALIGNMENTS = {
    'l' : 'left',
    'r' : 'right',
    'c' : 'center',
    'f' : 'float',
    'b' : 'bytes',
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

# (o-----------------------------------------------------------/\-----o)
#   CELULARTABLE SECTION (END)
# (o==================================================================o)