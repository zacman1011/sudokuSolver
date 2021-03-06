from Cell import Cell
from Line import Line


class Board:

    def __init__(self, initial_puzzle):
        self.whole_board = []
        self.rows = []
        self.columns = []

        for row in initial_puzzle:
            curr_row = []
            for num in row:
                cell = Cell(num)
                curr_row.append(cell)
            self.whole_board += curr_row
            self.rows.append(Line(curr_row))

        for i in range(9):
            curr_column = []
            for j in range(9):
                cell = self.whole_board[j*9 + i]
                curr_column.append(cell)
            self.columns.append(Line(curr_column))

        # set up boxes in init

    def step(self):
        return
        # have each line step
        # have each box step
        # have each cell step

    def __str__(self):
        output = ""
        for row in self.rows:
            output += str(row) + "\n"
        return output
