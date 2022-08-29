from typing import Any, List, Tuple, Union

from utils.micro_classes import Empty

from .type_parsers import (
    is_none,
    is_bool,
    is_int,
    is_float,
    is_exponential,
)
from utils.constants import (
    TYPE_NAMES,
    TYPE_NAME_I,
    TYPE_PARSER_I,
)


# Type hierarchy for this package
#   None
#   bool
#   int
#   float | exponential
#   str
#   (Any other)


__fast_check = { True: None }
__is_empty = {Empty: None}

__parse_groups = {
    TYPE_NAMES.none_type_: is_none,
    TYPE_NAMES.bool_: is_bool,
    TYPE_NAMES.int_: is_int,
    TYPE_NAMES.float_: is_float,
    TYPE_NAMES.exponential: is_exponential,
}


def try_evey_type(piece: Any):
    try:
        __is_empty[piece]
        return TYPE_NAMES.empty
    except KeyError:
        pass
    for parse_group in __parse_groups.items():
        match = __use_parse_group(parse_group, piece)
        try:
            __parse_groups[match]
            return match
        except KeyError:
            pass
    else:
        return TYPE_NAMES.str_
    

def __use_parse_group(parse_group: Tuple[str, 'function'],
                      piece: Any,
                     ) -> Union[str, None]:
    type_name = parse_group[TYPE_NAME_I]
    parser_function = parse_group[TYPE_PARSER_I]
    result: bool = parser_function(piece)
    try:
        __fast_check[result]  # If result is True
        return type_name
    except KeyError:
        return TYPE_NAMES.no_match  # If result is False
    

def get_column_type_name(column: List[str]) -> str:
    is_none = TYPE_NAMES.none_type_ in column
    is_bool = TYPE_NAMES.bool_ in column
    is_int = TYPE_NAMES.int_ in column
    is_float = TYPE_NAMES.float_ in column
    is_exponential = TYPE_NAMES.exponential in column
    
    try:
        __fast_check[is_none]
        return TYPE_NAMES.none_type_
    except KeyError:
        pass
    try:
        __fast_check[is_bool]
        return TYPE_NAMES.bool_
    except KeyError:
        pass
    try:
        __fast_check[is_int]
        return TYPE_NAMES.int_
    except KeyError:
        pass
    try:
        __fast_check[is_float]
        return TYPE_NAMES.float_
    except KeyError:
        pass
    try:
        __fast_check[is_exponential]
        return TYPE_NAMES.exponential
    except KeyError:
        pass
    
    return TYPE_NAMES.str_
    
    