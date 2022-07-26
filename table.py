from typing import List

from cell import Cell
from constants import (
    AT_LEAST_THREE,
    UPPER_LOWER_CELL_ROW_HEIGHT,
    PENULT_CELL_ROW_HEIGHT,
    SECOND_TO_ANTE_PENULT,
    AT_LEAST_ONE,
    AT_LEAST_TWO,
    AT_LEAST_FOUR,
    FIRST,
    PENULT,
    LAST,
)


class CelularTable:
    
    def __init__(self) -> None:
        self.headers = ['HEADER1', 'HEADER2']
        self.rows = [
            ['Primer Nombre', 20, 'Ciudad'],
            ['Nombre Hipotético', 45, 'Ciudad'],
            ['Otro Más', 37, 'Ciudad'],
            ['Último Ya', 24, 'Ciudad'],
        ]
        self.column_count = 3
        self.row_count = 4
        self.show_headers = True
        self.column_alignments = ['l', 'r', 'l']
        self.column_widths = [20, 9, 10]
        self.__rows_config = {
            'upper': {
                'left_cell': self.__left_mid_upper_border_cell,
                'penult_cell': self.__penult_upper_border_cell,
                'right_cell': self.__right_upper_border_cell,
                'row_height': UPPER_LOWER_CELL_ROW_HEIGHT,
            },
            'middle': {
                'left_cell': self.__left_mid_middle_cell,
                'penult_cell': self.__penult_middle_cell,
                'right_cell': self.__right_middle_cell,
                'row_height': UPPER_LOWER_CELL_ROW_HEIGHT,
            },
            'penult': {
                'left_cell': self.__left_mid_double_border_cell,
                'penult_cell': self.__penult_double_border_cell,
                'right_cell': self.__right_double_border_cell,
                'row_height': PENULT_CELL_ROW_HEIGHT,
            },
            'lower': {
                'left_cell': self.__left_mid_lower_border_cell,
                'penult_cell': self.__penult_lower_border_cell,
                'right_cell': self.__right_lower_border_cell,
                'row_height': UPPER_LOWER_CELL_ROW_HEIGHT,
            },
        }

    
    # (o==================================================================o)
    #   TABLE CRAFTING SECTION (START)
    #   processing of all the cells
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC INTERFACE ))
    
    def craft(self):
        all_rows = self.__create_all_rows(
            alignment=self.column_alignments,
            cols_widths=self.column_widths
        )
        headers = self.__create_row(
            **self.__rows_config['upper'],
            value=self.headers,
            alignment=self.column_alignments,
            width=self.column_widths,
            show_lower_border=[False]*self.column_count
            
        )
        print('\n'.join(headers))
        print('\n'.join(all_rows))

    # (o-----------------------------------------( PRIVATE ))
    
    def __create_all_rows(self, alignment, cols_widths):
        rows = []
        
        
        # UPPER ROW
        try:
            self.rows[AT_LEAST_TWO]
            rows.append('\n'.join(self.__create_row(
                **self.__rows_config['upper'],
                value=self.rows[FIRST],
                alignment=alignment,
                width=cols_widths,
                # show_upper_border=show_upper_border,
                )))
        except IndexError:
            pass
        
        # MIDDLE ROWS
        try:
            # At least four rows needed
            self.rows[AT_LEAST_FOUR]
            for mid_row in self.rows[SECOND_TO_ANTE_PENULT]:
                rows.append('\n'.join(self.__create_row(
                    **self.__rows_config['middle'],
                    value=mid_row,
                    alignment=alignment,
                    width=cols_widths
                )))
        except IndexError:
            pass
        
        # PENULT ROW
        try:
            self.rows[AT_LEAST_THREE]
            rows.append('\n'.join(self.__create_row(
                **self.__rows_config['penult'],
                value=self.rows[PENULT],
                alignment=alignment,
                width=cols_widths
            )))
        except IndexError:
            try:
                self.rows[AT_LEAST_ONE]
                rows.append('\n'.join(self.__create_row(
                    **self.__rows_config['penult'],
                    value=self.rows[LAST],
                    alignment=alignment,
                    width=cols_widths
                )))
            except IndexError:
                pass
        
        # LOWER ROW
        try:
            self.rows[AT_LEAST_THREE]
            rows.append('\n'.join(self.__create_row(
                **self.__rows_config['lower'],
                value=self.rows[LAST],
                alignment=alignment,
                width=cols_widths
            )))
        except IndexError:
            pass
        
        return rows
            
    def __cell_row_config(self, 
                          cell_quantity: int,
                          left,
                          penult,
                          right,
                         ) -> list:
        row_config = []
        if cell_quantity == 1:
            row_config.append(penult)
        elif cell_quantity >= 2:
            left_to_ante_penult = cell_quantity - 2
            for _ in range(left_to_ante_penult):
                row_config.append(
                    left
                )
            row_config.append(penult)
            row_config.append(right)
        
        return row_config
    
    def __create_row(self, 
                     left_cell,
                     penult_cell,
                     right_cell,
                     row_height,
                     **cells_parameters
                     ) -> List[str]:
        """
        Pass parameters to modify the cell of each value as a list
        of the same size as the values.
        
        Cell parameters::
            
            alignment
            value
            width
            left_width
            right_width
            up_width
            down_width
            up_left_corner_width
            up_right_corner_width
            down_left_corner_width
            down_right_corner_width
            align_sign_left_width
            align_sign_right_width
            align_sign_center_width
            bold_text
            show_upper_border
            show_left_border
            show_lower_border
            show_right_border
            show_upper_align_sign
            show_lower_align_sign
            persistent_cell_size
            keep_upper_left_corner
            keep_upper_right_corner
            keep_lower_left_corner
            keep_lower_right_corner
        """
        try:
            quantity_of_values = cells_parameters['value'].__len__()
            cells_to_craft = cells_parameters['value']
        except KeyError:
            quantity_of_values = 0
            cells_to_craft = []
        row_config = self.__cell_row_config(
            cell_quantity=quantity_of_values,
            left=left_cell,
            penult=penult_cell,
            right=right_cell,
        )
        
        param_groups = self.__get_groups_of_parameters(cells_parameters)
        unjoined_cells = []
        for cell_config_i, _ in enumerate(cells_to_craft):
            cell_creator = row_config[cell_config_i]
            obj_cell: Cell = self.__create_cell(
                cell_creator=cell_creator,
                parameters=param_groups[cell_config_i]
            )
            cell_parts = obj_cell.craft()
            unjoined_cells.append(cell_parts)
            
        
        joined_cell_parts = []
        for part_i in range(row_height):
            joined_part = ''.join(list(
                map(
                    lambda cell: cell[part_i], 
                    unjoined_cells
                )
            ))
            joined_cell_parts.append(joined_part)
        

        return joined_cell_parts
    
    @staticmethod
    def __get_groups_of_parameters(parameters: dict) -> List[dict]:
        keys = list(parameters.keys())
        values = list(parameters.values())
        column_quantity = parameters['value'].__len__()
        
        param_groups = []
        [param_groups.append({}) for _ in range(column_quantity)]
        for key_i, key in enumerate(keys):
            for column_i in range(column_quantity):
                param_groups[column_i][key] = values[key_i][column_i]
                        
        return param_groups
        
    
    def __create_cell(self, cell_creator, parameters: dict) -> Cell:
        return cell_creator(parameters)
    
    # (o-----------------------------------------------------------/\-----o)
    #   TABLE CRAFTING SECTION (END)
    # (o==================================================================o)
    
    @staticmethod
    def __add_cell_params(cell: Cell, params: dict):
        try:
            cell.alignment = params['alignment']
        except KeyError:
            pass
        try:
            cell.value = params['value']
        except KeyError:
            pass
        try:
            cell.width = params['width']
        except KeyError:
            pass
        try:
            cell.left_width = params['left_width']
        except KeyError:
            pass
        try:
            cell.right_width = params['right_width']
        except KeyError:
            pass
        try:
            cell.up_width = params['up_width']
        except KeyError:
            pass
        try:
            cell.down_width = params['down_width']
        except KeyError:
            pass
        try:
            cell.up_left_corner_width = params['up_left_corner_width']
        except KeyError:
            pass
        try:
            cell.up_right_corner_width = params['up_right_corner_width']
        except KeyError:
            pass
        try:
            cell.down_left_corner_width = params['down_left_corner_width']
        except KeyError:
            pass
        try:
            cell.down_right_corner_width = params['down_right_corner_width']
        except KeyError:
            pass
        try:
            cell.align_sign_left_width = params['align_sign_left_width']
        except KeyError:
            pass
        try:
            cell.align_sign_right_width = params['align_sign_right_width']
        except KeyError:
            pass
        try:
            cell.align_sign_center_width = params['align_sign_center_width']
        except KeyError:
            pass
        try:
            cell.bold_text = params['bold_text']
        except KeyError:
            pass
        try:
            cell.show_upper_border = params['show_upper_border']
        except KeyError:
            pass
        try:
            cell.show_left_border = params['show_left_border']
        except KeyError:
            pass
        try:
            cell.show_lower_border = params['show_lower_border']
        except KeyError:
            pass
        try:
            cell.show_right_border = params['show_right_border']
        except KeyError:
            pass
        try:
            cell.show_upper_align_sign = params['show_upper_align_sign']
        except KeyError:
            pass
        try:
            cell.show_lower_align_sign = params['show_lower_align_sign']
        except KeyError:
            pass
        try:
            cell.persistent_cell_size = params['persistent_cell_size']
        except KeyError:
            pass
        try:
            cell.keep_upper_left_corner = params['keep_upper_left_corner']
        except KeyError:
            pass
        try:
            cell.keep_upper_right_corner = params['keep_upper_right_corner']
        except KeyError:
            pass
        try:
            cell.keep_lower_left_corner = params['keep_lower_left_corner']
        except KeyError:
            pass
        try:
            cell.keep_lower_right_corner = params['keep_lower_right_corner']
        except KeyError:
            pass
        
        return cell

    # (o==================================================================o)
    #   UPPER ROW CRAFTING SECTION (START)
    #   upper and middle rows of cells
    # (o-----------------------------------------------------------\/-----o)
    
    def __left_mid_upper_border_cell(self, params: dict) -> Cell:
        left_cell = Cell()
        left_cell.show_right_border = False
        left_cell.show_lower_border = False
        left_cell = self.__add_cell_params(left_cell, params)

        return left_cell
    
    def __penult_upper_border_cell(self, params: dict) -> Cell:
        penult_cell = Cell()
        penult_cell.show_lower_border = False
        penult_cell = self.__add_cell_params(penult_cell, params)
        
        return penult_cell

    def __right_upper_border_cell(self, params: dict) -> Cell:
        right_cell = Cell()
        right_cell.show_left_border = False
        right_cell.show_lower_border = False
        right_cell = self.__add_cell_params(right_cell, params)

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   UPPER ROW CRAFTING SECTION (END)
    # (o==================================================================o)


    # (o==================================================================o)
    #   MIDDLE ROW CRAFTING SECTION (START)
    #   upper and middle rows of cells
    # (o-----------------------------------------------------------\/-----o)
    
    def __left_mid_middle_cell(self, params: dict) -> Cell:
        left_cell = Cell()
        left_cell.show_right_border = False
        left_cell.show_lower_border = False
        left_cell = self.__add_cell_params(left_cell, params)

        return left_cell
    
    def __penult_middle_cell(self, params: dict) -> Cell:
        penult_cell = Cell()
        penult_cell.show_lower_border = False
        penult_cell = self.__add_cell_params(penult_cell, params)
        
        return penult_cell

    def __right_middle_cell(self, params: dict) -> Cell:
        right_cell = Cell()
        right_cell.show_left_border = False
        right_cell.show_lower_border = False
        right_cell = self.__add_cell_params(right_cell, params)

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   MIDDLE ROW CRAFTING SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   PENULT ROW CRAFTING SECTION (START)
    #   penult rows of cells
    # (o-----------------------------------------------------------\/-----o)
       
    def __left_mid_double_border_cell(self, params: dict) -> Cell:
        left_cell = Cell()
        left_cell.show_right_border = False
        left_cell = self.__add_cell_params(left_cell, params)

        return left_cell
    
    def __penult_double_border_cell(self, params: dict) -> Cell:
        penult_cell = Cell()
        penult_cell = self.__add_cell_params(penult_cell, params)
        
        return penult_cell

    def __right_double_border_cell(self, params: dict) -> Cell:
        right_cell = Cell()
        right_cell.show_left_border = False
        right_cell = self.__add_cell_params(right_cell, params)

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   PENULT ROW CRAFTING SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   LOWER ROW CRAFTING SECTION (START)
    #   lower row of cells
    # (o-----------------------------------------------------------\/-----o)

    def __left_mid_lower_border_cell(self, params: dict) -> Cell:
        left_cell = Cell()
        left_cell.show_right_border = False
        left_cell.show_upper_border = False
        left_cell = self.__add_cell_params(left_cell, params)

        return left_cell
    
    def __penult_lower_border_cell(self, params: dict) -> Cell:
        penult_cell = Cell()
        penult_cell.show_upper_border = False
        penult_cell = self.__add_cell_params(penult_cell, params)
        
        return penult_cell

    def __right_lower_border_cell(self, params: dict) -> Cell:
        right_cell = Cell()
        right_cell.show_left_border = False
        right_cell.show_upper_border = False
        right_cell = self.__add_cell_params(right_cell, params)

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   LOWER ROW CRAFTING SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   SPECIAL CELL CASES CRAFTING SECTION (START)
    #   special cell structures that are needed in unique situations
    # (o-----------------------------------------------------------\/-----o)
    
    # def __empty_header_cell(self, params: dict) -> Cell:
    #     empty_h_cell = Cell()
    #     empty_h_cell.show_upper_border = False
    #     empty_h_cell.show_left_border = False
    #     empty_h_cell.show_right_border = False
    #     empty_h_cell = self.__add_cell_params(empty_h_cell, params)
        
    #     return empty_h_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   SPECIAL CELL CASES CRAFTING SECTION (END)
    # (o==================================================================o)
        
        
    
