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
        self.show_headers = True
        self.__rows_config = {
            'upper': [
                self.__left_mid_upper_border_cell,
                self.__penult_upper_border_cell,
                self.__right_upper_border_cell,
                UPPER_LOWER_CELL_ROW_HEIGHT,
            ],
            'middle': [
                self.__left_mid_middle_cell,
                self.__penult_middle_cell,
                self.__right_middle_cell,
                UPPER_LOWER_CELL_ROW_HEIGHT,
            ],
            'penult': [
                self.__left_mid_double_border_cell,
                self.__penult_double_border_cell,
                self.__right_double_border_cell,
                PENULT_CELL_ROW_HEIGHT,
            ],
            'lower': [
                self.__left_mid_lower_border_cell,
                self.__penult_lower_border_cell,
                self.__right_lower_border_cell,
                UPPER_LOWER_CELL_ROW_HEIGHT
            ]
        }

    
    # (o==================================================================o)
    #   TABLE CRAFTING SECTION (START)
    #   processing of all the cells
    # (o-----------------------------------------------------------\/-----o)
    
    # (o-----------------------------------------( PUBLIC INTERFACE ))
    
    def craft(self):
        all_rows = self.__create_all_rows()
        print('\n'.join(all_rows))
        
    # (o-----------------------------------------( PRIVATE ))
    
    def __create_all_rows(self):
        rows = []
        
        # UPPER ROW
        try:
            # At least two rows needed
            self.rows[AT_LEAST_TWO]
            rows.append('\n'.join(self.__create_row(
                *self.__rows_config['upper'],
                self.rows[FIRST],
            )))
        except IndexError:
            pass
        
        # MIDDLE ROWS
        try:
            # At least four rows needed
            self.rows[AT_LEAST_FOUR]
            for mid_row in self.rows[SECOND_TO_ANTE_PENULT]:
                rows.append('\n'.join(self.__create_row(
                    *self.__rows_config['middle'],
                    mid_row,
                )))
        except IndexError:
            pass
        
        # PENULT ROW
        try:
            self.rows[AT_LEAST_THREE]
            rows.append('\n'.join(self.__create_row(
                *self.__rows_config['penult'],
                self.rows[PENULT],
            )))
        except IndexError:
            try:
                self.rows[AT_LEAST_ONE]
                rows.append('\n'.join(self.__create_row(
                    *self.__rows_config['penult'],
                    self.rows[LAST],
                )))
            except IndexError:
                pass
        
        # LOWER ROW
        try:
            self.rows[AT_LEAST_THREE]
            rows.append('\n'.join(self.__create_row(
                *self.__rows_config['lower'],
                self.rows[LAST],
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
                     values,
                     ) -> List[str]:
        row_config = self.__cell_row_config(
            cell_quantity=values.__len__(),
            left=left_cell,
            penult=penult_cell,
            right=right_cell,
        )
        unjoined_cells = []
        for cell_config_i, value in enumerate(values):
            cell = row_config[cell_config_i]
            obj_cell: Cell = cell(value, 'c', 20)
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
    
    # (o-----------------------------------------------------------/\-----o)
    #   TABLE CRAFTING SECTION (END)
    # (o==================================================================o)


    # (o==================================================================o)
    #   UPPER ROW CRAFTING SECTION (START)
    #   upper and middle rows of cells
    # (o-----------------------------------------------------------\/-----o)
    
    @staticmethod
    def __left_mid_upper_border_cell(value, 
                                     align: str, 
                                     width: int
                                    ) -> Cell:
        left_cell = Cell()
        left_cell.value = value
        left_cell.alignment = align
        left_cell.width = width
        left_cell.show_right_border = False
        left_cell.show_lower_border = False

        return left_cell
    
    @staticmethod
    def __penult_upper_border_cell(value, 
                                   align: str, 
                                   width: int
                                  ) -> Cell:
        penult_cell = Cell()
        penult_cell.value = value
        penult_cell.alignment = align
        penult_cell.width = width
        penult_cell.show_lower_border = False
        
        return penult_cell

    @staticmethod
    def __right_upper_border_cell(value, 
                                  align: str, 
                                  width: int
                                 ) -> Cell:
        right_cell = Cell()
        right_cell.value = value
        right_cell.alignment = align
        right_cell.width = width
        right_cell.show_left_border = False
        right_cell.show_lower_border = False

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   UPPER ROW CRAFTING SECTION (END)
    # (o==================================================================o)


    # (o==================================================================o)
    #   MIDDLE ROW CRAFTING SECTION (START)
    #   upper and middle rows of cells
    # (o-----------------------------------------------------------\/-----o)
    
    @staticmethod
    def __left_mid_middle_cell(value, 
                               align: str, 
                               width: int
                              ) -> Cell:
        left_cell = Cell()
        left_cell.value = value
        left_cell.alignment = align
        left_cell.width = width
        left_cell.show_right_border = False
        left_cell.show_lower_border = False

        return left_cell
    
    @staticmethod
    def __penult_middle_cell(value, 
                             align: str, 
                             width: int
                              ) -> Cell:
        penult_cell = Cell()
        penult_cell.value = value
        penult_cell.alignment = align
        penult_cell.width = width
        penult_cell.show_lower_border = False
        
        return penult_cell

    @staticmethod
    def __right_middle_cell(value, 
                            align: str, 
                            width: int
                          ) -> Cell:
        right_cell = Cell()
        right_cell.value = value
        right_cell.alignment = align
        right_cell.width = width
        right_cell.show_left_border = False
        right_cell.show_lower_border = False

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   MIDDLE ROW CRAFTING SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   PENULT ROW SECTION (START)
    #   penult rows of cells
    # (o-----------------------------------------------------------\/-----o)
       
    @staticmethod
    def __left_mid_double_border_cell(value, 
                                      align: str, 
                                      width: int
                                     ) -> Cell:
        left_cell = Cell()
        left_cell.value = value
        left_cell.alignment = align
        left_cell.width = width
        left_cell.show_right_border = False

        return left_cell
    
    @staticmethod
    def __penult_double_border_cell(value, 
                                    align: str, 
                                    width: int
                                   ) -> Cell:
        penult_cell = Cell()
        penult_cell.value = value
        penult_cell.alignment = align
        penult_cell.width = width
        
        return penult_cell

    @staticmethod
    def __right_double_border_cell(value, 
                                   align: str, 
                                   width: int
                                  ) -> Cell:
        right_cell = Cell()
        right_cell.value = value
        right_cell.alignment = align
        right_cell.width = width
        right_cell.show_left_border = False

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   PENULT ROW SECTION (END)
    # (o==================================================================o)
    
    
    # (o==================================================================o)
    #   LOWER ROW CRAFTING SECTION (START)
    #   lower row of cells
    # (o-----------------------------------------------------------\/-----o)

    @staticmethod
    def __left_mid_lower_border_cell(value, 
                                     align: str, 
                                     width: int
                                    ) -> Cell:
        left_cell = Cell()
        left_cell.value = value
        left_cell.alignment = align
        left_cell.width = width
        left_cell.show_right_border = False
        left_cell.show_upper_border = False

        return left_cell
    
    @staticmethod
    def __penult_lower_border_cell(value, 
                                   align: str, 
                                   width: int
                                  ) -> Cell:
        penult_cell = Cell()
        penult_cell.value = value
        penult_cell.alignment = align
        penult_cell.width = width
        penult_cell.show_upper_border = False
        
        return penult_cell

    @staticmethod
    def __right_lower_border_cell(value, 
                                  align: str, 
                                  width: int
                                 ) -> Cell:
        right_cell = Cell()
        right_cell.value = value
        right_cell.alignment = align
        right_cell.width = width
        right_cell.show_left_border = False
        right_cell.show_upper_border = False

        return right_cell
    
    # (o-----------------------------------------------------------/\-----o)
    #   LOWER ROW CRAFTING SECTION (END)
    # (o==================================================================o)
        
        
    
