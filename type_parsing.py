import re

# Type hierarchy for this package
#   None
#   bool
#   int
#   float
#   str
#   (Any other)

def try_regex(regex_string, value):
    searcher = re.compile(regex_string, re.VERBOSE)
    try:
        match = searcher.match(value.strip())
        match_width = match.end() - match.start()
        full_match = value.strip().__len__() == match_width
    except (TypeError, AttributeError):
        pass
    try:
        value_ = str(value)
        match = searcher.match(str(value_).strip())
        match_width = match.end() - match.start()
        full_match = str(value_).strip().__len__() == match_width
    except AttributeError:
        full_match = False
        
    return full_match


def is_bool(value):
    return try_regex(
        r"""            # === CASE 1 ===
            [ ]*        # Any space before.
            \bTrue\b    # Exact word "True".
            |           # === CASE 2 ===
            [ ]*        # Any space before.
            \bFalse\b   # Exact word "False".
         """, 
        value
    )


def is_int(value):
    return try_regex(
        r"""
            ^
            [-]?                # Optional negative sign.
            [0-9]([_]?[0-9])*   # Number group.
            $
         """, 
        value
    )

        
def is_float(value):
    return try_regex(
        r"""
            ^
            [ ]*                    # Any space before.
            [-]?                    # Optional negative sign.
            ([0-9]([_]?[0-9])*)*    # Number group.
            [.]                     # Dot.
            ([0-9]([_]?[0-9])*)*    # Number group.
            [ ]*                    # Any space after.
            $
         """, 
        value
    )


def is_exponential(value):
    return try_regex(
        r"""
            ^                               
            [ ]*                            # Any space before.
            
            ([-]?                           # Optional negative sign.       |
             ((([0-9]([_]?[0-9])*)*         # Number group. |               |
                [.]                         # Dot.          +---+ FLOAT     |
                ([-]?[0-9]([_]?[0-9])*)*)   # Number group. |               |---+ FLOAT or
               |                            # == OR ==                      |     INT before
               ([0-9]([_]?[0-9])*))         # Number group. +---+ INT       |     the "e"
             
             [eE]                           # The "e" or "E" (exponential). 
             
             [-]?                           # Optional negative sign.       |---+ INT after
             ([0-9]([_]?[0-9])*))           # Number group.                 | 
             
            [ ]*                            # Any space after.
            $
         """,
         value
    )

    