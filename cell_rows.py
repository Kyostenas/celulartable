from cell import Cell
from constants import (
    PENULT_CELL_ROW_HEIGHT, 
    UPPER_LOWER_CELL_ROW_HEIGHT
)


def create_rows_config() -> dict:
    return  {
        'header': {
            'left_cell': left_mid_header_cell,
            'penult_cell': penult_header_cell,
            'right_cell': right_header_cell,
            'row_height':UPPER_LOWER_CELL_ROW_HEIGHT,
        },
        'upper': {
            'left_cell': left_mid_upper_border_cell,
            'penult_cell': penult_upper_border_cell,
            'right_cell': right_upper_border_cell,
            'row_height': UPPER_LOWER_CELL_ROW_HEIGHT,
        },
        'middle': {
            'left_cell': left_mid_middle_cell,
            'penult_cell': penult_middle_cell,
            'right_cell': right_middle_cell,
            'row_height': UPPER_LOWER_CELL_ROW_HEIGHT,
        },
        'penult': {
            'left_cell': left_mid_double_border_cell,
            'penult_cell': penult_double_border_cell,
            'right_cell': right_double_border_cell,
            'row_height': PENULT_CELL_ROW_HEIGHT,
        },
        'lower': {
            'left_cell': left_mid_lower_border_cell,
            'penult_cell': penult_lower_border_cell,
            'right_cell': right_lower_border_cell,
            'row_height': UPPER_LOWER_CELL_ROW_HEIGHT,
        },
    }


def add_cell_params(cell: Cell, params: dict):
    for param_name, param in params.items():
        cell.__setattr__(param_name, param)
    
    return cell

    
def upper_border_bold_if_header(cell: Cell) -> Cell:
    # if self.headers is not None and self.show_headers:
    cell.up_right_corner_width = 'bold'
    cell.up_left_corner_width = 'bold'
    cell.up_width = 'bold'

    return cell
    
    
# (o==================================================================o)
#   HEADER ROW CRAFTING SECTION (START)
#   upper and middle rows of cells
# (o-----------------------------------------------------------\/-----o)


def left_mid_header_cell(params: dict) -> Cell:
    left_cell = Cell()
    left_cell.show_right_border = False
    left_cell.show_lower_border = False
    left_cell = add_cell_params(left_cell, params)

    return left_cell


def penult_header_cell(params: dict) -> Cell:
    penult_cell = Cell()
    penult_cell.show_lower_border = False
    penult_cell = add_cell_params(penult_cell, params)
    
    return penult_cell


def right_header_cell(params: dict) -> Cell:
    right_cell = Cell()
    right_cell.show_left_border = False
    right_cell.show_lower_border = False
    right_cell = add_cell_params(right_cell, params)

    return right_cell


# (o-----------------------------------------------------------/\-----o)
#   HEADER ROW CRAFTING SECTION (END)
# (o==================================================================o)


# (o==================================================================o)
#   UPPER ROW CRAFTING SECTION (START)
#   upper and middle rows of cells
# (o-----------------------------------------------------------\/-----o)

def left_mid_upper_border_cell(params: dict) -> Cell:
    left_cell = Cell()
    left_cell.show_right_border = False
    left_cell.show_lower_border = False
    left_cell = upper_border_bold_if_header(left_cell)
    left_cell = add_cell_params(left_cell, params)

    return left_cell


def penult_upper_border_cell(params: dict) -> Cell:
    penult_cell = Cell()
    penult_cell.show_lower_border = False
    penult_cell = upper_border_bold_if_header(penult_cell)
    penult_cell = add_cell_params(penult_cell, params)
    
    return penult_cell


def right_upper_border_cell(params: dict) -> Cell:
    right_cell = Cell()
    right_cell.show_left_border = False
    right_cell.show_lower_border = False
    right_cell = upper_border_bold_if_header(right_cell)
    right_cell = add_cell_params(right_cell, params)

    return right_cell


# (o-----------------------------------------------------------/\-----o)
#   UPPER ROW CRAFTING SECTION (END)
# (o==================================================================o)


# (o==================================================================o)
#   MIDDLE ROW CRAFTING SECTION (START)
#   upper and middle rows of cells
# (o-------------
# ----------------------------------------------\/-----o)

def left_mid_middle_cell(params: dict) -> Cell:
    left_cell = Cell()
    left_cell.show_right_border = False
    left_cell.show_lower_border = False
    left_cell = add_cell_params(left_cell, params)

    return left_cell


def penult_middle_cell(params: dict) -> Cell:
    penult_cell = Cell()
    penult_cell.show_lower_border = False
    penult_cell = add_cell_params(penult_cell, params)
    
    return penult_cell


def right_middle_cell(params: dict) -> Cell:
    right_cell = Cell()
    right_cell.show_left_border = False
    right_cell.show_lower_border = False
    right_cell = add_cell_params(right_cell, params)

    return right_cell


# (o-----------------------------------------------------------/\-----o)
#   MIDDLE ROW CRAFTING SECTION (END)
# (o==================================================================o)


# (o==================================================================o)
#   PENULT ROW CRAFTING SECTION (START)
#   penult rows of cells
# (o-----------------------------------------------------------\/-----o)
    
    
def left_mid_double_border_cell(params: dict) -> Cell:
    left_cell = Cell()
    left_cell.show_right_border = False
    left_cell = add_cell_params(left_cell, params)

    return left_cell


def penult_double_border_cell(params: dict) -> Cell:
    penult_cell = Cell()
    penult_cell = add_cell_params(penult_cell, params)
    
    return penult_cell


def right_double_border_cell(params: dict) -> Cell:
    right_cell = Cell()
    right_cell.show_left_border = False
    right_cell = add_cell_params(right_cell, params)

    return right_cell


# (o-----------------------------------------------------------/\-----o)
#   PENULT ROW CRAFTING SECTION (END)
# (o==================================================================o)


# (o==================================================================o)
#   LOWER ROW CRAFTING SECTION (START)
#   lower row of cells
# (o-----------------------------------------------------------\/-----o)


def left_mid_lower_border_cell(params: dict) -> Cell:
    left_cell = Cell()
    left_cell.show_right_border = False
    left_cell.show_upper_border = False
    left_cell = add_cell_params(left_cell, params)

    return left_cell


def penult_lower_border_cell(params: dict) -> Cell:
    penult_cell = Cell()
    penult_cell.show_upper_border = False
    penult_cell = add_cell_params(penult_cell, params)
    
    return penult_cell


def right_lower_border_cell(params: dict) -> Cell:
    right_cell = Cell()
    right_cell.show_left_border = False
    right_cell.show_upper_border = False
    right_cell = add_cell_params(right_cell, params)

    return right_cell


# (o-----------------------------------------------------------/\-----o)
#   LOWER ROW CRAFTING SECTION (END)
# (o==================================================================o)


# (o==================================================================o)
#   SPECIAL CELL CASES CRAFTING SECTION (START)
#   special cell structures that are needed in unique situations
# (o-----------------------------------------------------------\/-----o)


def empty_cell(params: dict) -> Cell:
    empty_cell = Cell()
    empty_cell.show_upper_border = False
    empty_cell.show_left_border = False
    empty_cell.show_right_border = False
    empty_cell.show_lower_border = False
    empty_cell = add_cell_params(empty_cell, params) 


# (o-----------------------------------------------------------/\-----o)
#   SPECIAL CELL CASES CRAFTING SECTION (END)
# (o==================================================================o)