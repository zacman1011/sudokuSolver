from Box import Box
from Cell import Cell
from Line import Line


class Board:

    def __init__(self, initial_puzzle):
        self.whole_board = []
        self.rows = []
        self.columns = []
        self.boxes = []
        self.finished = False

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
                cell = self.whole_board[j * 9 + i]
                curr_column.append(cell)
            self.columns.append(Line(curr_column))

        self.boxes.append(Box([self.whole_board[0], self.whole_board[1], self.whole_board[2],
                               self.whole_board[9], self.whole_board[10], self.whole_board[11],
                               self.whole_board[18], self.whole_board[19], self.whole_board[20]]))  # box TL
        self.boxes.append(Box([self.whole_board[27], self.whole_board[28], self.whole_board[29],
                               self.whole_board[36], self.whole_board[37], self.whole_board[38],
                               self.whole_board[45], self.whole_board[46], self.whole_board[47]]))  # box ML
        self.boxes.append(Box([self.whole_board[54], self.whole_board[55], self.whole_board[56],
                               self.whole_board[63], self.whole_board[64], self.whole_board[65],
                               self.whole_board[72], self.whole_board[73], self.whole_board[74]]))  # box BL

        self.boxes.append(Box([self.whole_board[3], self.whole_board[4], self.whole_board[5],
                               self.whole_board[12], self.whole_board[13], self.whole_board[14],
                               self.whole_board[21], self.whole_board[22], self.whole_board[23]]))  # box TM
        self.boxes.append(Box([self.whole_board[30], self.whole_board[4], self.whole_board[5],
                               self.whole_board[39], self.whole_board[13], self.whole_board[14],
                               self.whole_board[48], self.whole_board[22], self.whole_board[23]]))  # box MM
        self.boxes.append(Box([self.whole_board[57], self.whole_board[58], self.whole_board[59],
                               self.whole_board[66], self.whole_board[67], self.whole_board[68],
                               self.whole_board[75], self.whole_board[76], self.whole_board[77]]))  # box BM

        self.boxes.append(Box([self.whole_board[6], self.whole_board[7], self.whole_board[8],
                               self.whole_board[15], self.whole_board[16], self.whole_board[17],
                               self.whole_board[24], self.whole_board[25], self.whole_board[26]]))  # box TR
        self.boxes.append(Box([self.whole_board[33], self.whole_board[34], self.whole_board[35],
                               self.whole_board[42], self.whole_board[43], self.whole_board[44],
                               self.whole_board[51], self.whole_board[52], self.whole_board[53]]))  # box MR
        self.boxes.append(Box([self.whole_board[60], self.whole_board[61], self.whole_board[62],
                               self.whole_board[69], self.whole_board[70], self.whole_board[71],
                               self.whole_board[78], self.whole_board[79], self.whole_board[80]]))  # box BR

    def step(self):
        for box in self.boxes:
            box.step()

        for row in self.rows:
            row.step()

        for column in self.columns:
            column.step()

        finished = True
        for cell in self.whole_board:
            finished = finished and cell.step()
        self.finished = finished

    def __str__(self):
        output = ""
        for row in self.rows:
            output += str(row) + "\n"
        return output
