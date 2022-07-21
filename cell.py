
from typing import Dict, Tuple

from cell_styles import (
    style_names,
    Style
)
from constants import (
    ALIGNMENTS,
    BOLD_WIDTH_NAME,
    CENTERED,
    DEFAULT_CELL_ALIGNMENT,
    DEFAULT_MISSING_VALUE,
    DEFAULT_STYLE_NAME,
    LEFT_ALIGNED,
    RIGHT_ALIGNED,
    THIN_WIDTH_NAME,
    TO_CENTER,
    TO_RIGHT_ALIGN
)

class Cell:
    
    def __init__(self) -> None:
        self.__style_name: str = DEFAULT_STYLE_NAME
        self.__value = DEFAULT_MISSING_VALUE
        self.__width: int = 0
        self.__border_width: Dict[str, bool] = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'up_left_corner': False,
            'up_right_corner': False,
            'down_left_corner': False,
            'down_right_corner': False,
            'align_sign_left': False,
            'align_sign_right': False,
            'align_sign_center': False,
        }
        self.__text_width: str = ''
        self.__formatted_value: str = ''
        self.__value_line: str = ''
        self.__upper_line: str = ''
        self.__lower_line: str = ''
        self.__alignment: str = DEFAULT_CELL_ALIGNMENT
        self.__float_column_widths: Tuple[int, int, int] = []
        
    def __call__(self, 
                 value, 
                 width: int,
                 bold_borders: Dict[str, bool] = {},
                 bold_text: bool = False,
                 text_color = None,
                 float_widths: Tuple[int, int, int] = []):
        """
        To set the width of the borders, add any of these
        keys to the bold_border parameter in a dict::
        
            'left'
            'right'
            'up'
            'down'
            'up_left_corner'
            'up_right_corner'
            'down_left_corner'
            'down_right_corner'
            'align_sign_left'
            'align_sign_right'
            'align_sign_center'

        """
        self.value = str(value)
        self.width = int(width)
        
        return self
        
    def craft(self):
        self.__format_value()
        self.__format_value_line()
        print(self.__value_line)
    
    # (o==================================================================o)
    #   CELL PROPERTIES SECTION (START)
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC ))
    
    @property
    def style(self) -> Style:
        return style_names[self.__style_name]
    
    @property
    def alignment(self) -> str:
        """
        The way the value is padded.

        One of::
        
            'l', 'r', 'c', 'f', 'b'
        """
        return self.__alignment
    
    # (o-----------------------------------------( PRIVATE ))
    
    
    # (o-----------------------------------------------------------/\-----o)
    #   CELL PROPERTIES SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   SETTERS SECTION (START)
    #   Setters for the Cell properties
    # (o-----------------------------------------------------------\/-----o)
    
    @alignment.setter
    def alignment(self, alignment) -> None:
        try:
            ALIGNMENTS[alignment]
            self.__alignment = alignment
        except KeyError:
            pass
    
    
    # (o-----------------------------------------------------------/\-----o)
    #   SETTERS SECTION (END)
    # (o==================================================================o)
    
    
    def __format_value(self) -> None:
        margin = self.style.margin
        width = self.width
        value = self.value
        alignment = self.__check_alignment()
        self.__formatted_value =  (
            f'{"":{margin}}{value:{alignment}{width}}{"":{margin}}'
        )   
    
    def __format_value_line(self) -> str:
        left = self.__get_border_part(
            self.style.left,
            'left'
        )
        right = self.__get_border_part(
            self.style.right,
            'right'
        )
        self.__value_line = (
            ''.join([left, self.__formatted_value, right])
        )
        
    def __get_border_part(self, part, part_name: str) -> str:
        width = self.__get_width(part_name)
        return part(width)
        
    def __get_width(self, part_name: str) -> str:
        if self.__border_width[part_name] is True:
            return BOLD_WIDTH_NAME
        else:
            return THIN_WIDTH_NAME
    
    def __check_alignment(self):
        if self.__alignment in TO_RIGHT_ALIGN:
            return RIGHT_ALIGNED
        elif self.__alignment in TO_CENTER:
            return CENTERED
        else:
            return LEFT_ALIGNED
    
    
    