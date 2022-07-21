
from typing import Dict, NamedTuple

# The composition of the style of a single cell
class Style(NamedTuple):
    ZZ_left: Dict[str, str]
    ZZ_right: Dict[str, str]
    ZZ_up: Dict[str, str]
    ZZ_down: Dict[str, str]
    ZZ_up_left_corner: Dict[str, str]
    ZZ_up_right_corner: Dict[str, str]
    ZZ_down_left_corner: Dict[str, str]
    ZZ_down_right_corner: Dict[str, str]
    ZZ_align_sign_left: Dict[str, str]
    ZZ_align_sign_right: Dict[str, str]
    ZZ_align_sign_center: Dict[str, str]
    margin: int
    
    def left(self, width):
        return self.ZZ_left[width]
    
    def right(self, width):
        return self.ZZ_right[width]

    def up(self, width):
        return self.ZZ_up[width]

    def down(self, width):
        return self.ZZ_down[width]

    def up_left_corner(self, width):
        return self.ZZ_up_left_corner[width]

    def up_right_corner(self, width):
        return self.ZZ_up_right_corner[width]

    def down_left_corner(self, width):
        return self.ZZ_down_left_corner[width]

    def down_right_corner(self, width):
        return self.ZZ_down_right_corner[width]

    def align_sign_left(self, width):
        return self.ZZ_align_sign_left[width]

    def align_sign_right(self, width):
        return self.ZZ_align_sign_right[width]

    def align_sign_center(self, width):
        return self.ZZ_align_sign_center[width]

    

# All the implemented styles
style_names = {
    'grid': Style(
        ZZ_left={'thin': '|', 'bold': '‖'},
        ZZ_right={'thin': '|', 'bold': '‖'},
        ZZ_up={'thin': '-', 'bold': '='},
        ZZ_down={'thin': '-', 'bold': '='},
        ZZ_up_left_corner={'thin': '+', 'bold': '#'},
        ZZ_up_right_corner={'thin': '+', 'bold': '#'},
        ZZ_down_left_corner={'thin': '+', 'bold': '#'},
        ZZ_down_right_corner={'thin': '+', 'bold': '#'},
        ZZ_align_sign_left={'thin': '‹', 'bold': '«'},
        ZZ_align_sign_right={'thin': '›', 'bold': '»'},
        ZZ_align_sign_center={'thin': '~', 'bold': '≈'},
        margin=1,
    )
}