from typing import List

from cell import Cell
from cell_rows import create_rows_config
from constants import (
    AT_LEAST_THREE,
    DEFAULT_MISSING_VALUE,
    SECOND_TO_ANTE_PENULT,
    AT_LEAST_ONE,
    AT_LEAST_TWO,
    AT_LEAST_FOUR,
    FIRST,
    PENULT,
    LAST,
)
from micro_classes import (
    Empty
)

class CelularTable:
    
    def __init__(self) -> None:
        self.headers = []
        self.rows = []
        self.column_count = 0
        self.row_count = 0
        self.show_headers = False
        self.column_alignments = []
        self.column_widths = []
        self.missing_value = DEFAULT_MISSING_VALUE
        self.__rows_config = create_rows_config()
        
        
    # (o==================================================================o)
    #   CELL ADDING SECTION (START)
    #   adding and processing of cells
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC INTERFACE ))
    
    def add_cell(self, 
                 value = Empty,
                 row_i: int = None, 
                 column_i: int = None, 
                ) -> None:
        value = self.__validate_value(value)
        row_i = self.__validate_row_i(row_i)
        column_i = self.__validate_column_i(row_i, column_i)
        self.__add_value_to_row(value, row_i, column_i)
    
    def add_header_cell(self, 
                        value = None,
                        column_i: int = None, 
                       ) -> None:
        column_i = self.__validate_header_column_i(column_i)
        self.headers.insert(column_i, value)
        
    def add_row(self,
                data: list,
                row_i: int = None,
               ) -> None:
        for piece in data:
            self.add_cell(
                value=piece, 
                row_i=row_i
            )
            
    def add_headers(self, headers: list) -> None:
        for header in headers:
            self.add_header_cell(header)
        
    # (o-----------------------------------------( PRIVATE ))
    
    def __validate_value(self, value):
        if value is Empty:
            value = self.missing_value
        return value
      
    def __add_value_to_row(self,
                           value,
                           row_i: int,
                           column_i: int,
                          ) -> None:
        try:
            self.rows[row_i].insert(column_i, value)
        except IndexError:
            self.rows.append([])
            self.add_cell(
                value,
                row_i, 
                column_i, 
            )
    
    def __validate_row_i(self, row_i: int) -> int:
        if row_i is None:
            row_i = self.rows.__len__()
        if row_i + 1 > self.row_count:
            self.row_count = row_i + 1
        return row_i
            
    def __validate_column_i(self, row_i: int, column_i: int) -> int:
        if column_i is None:
            try:
                column_i = self.rows[row_i].__len__()
            except IndexError:
                column_i = 0
        if column_i + 1 > self.column_count:
            self.column_count = column_i + 1
        return column_i
    
    def __validate_header_column_i(self, column_i) -> int:
        if column_i is None:
            column_i = self.headers.__len__()
        if column_i + 1 > self.column_count:
            self.column_count = column_i + 1
        return column_i
    
    def __find_types(self):
        pass
    
    def __find_column_alignments(self):
        pass
    
    def __find_column_widths(self):
        pass
    
    
     
    # (o-----------------------------------------------------------/\-----o)
    #   CELL ADDING SECTION (END)
    # (o==================================================================o)

    
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
            **self.__rows_config['header'],
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
    


    

        
        
    
