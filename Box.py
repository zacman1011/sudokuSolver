class Box:

    def __init__(self, cells):
        self.cells = cells
        self.finished = False
        self.decided_nums = []

        for cell in cells:
            if cell.finished:
                self.decided_nums.append(cell.num)

        for cell in cells:
            if not cell.finished:
                cell.available = [num for num in cell.available if num not in self.decided_nums]

    def step(self):
        for cell in self.cells:
            if cell.finished and cell.num not in self.decided_nums:
                self.decided_nums.append(cell.num)

        for cell in self.cells:
            for num in self.decided_nums:
                if num in cell.available:
                    cell.available.remove(num)

        for i in range(9):
            if i not in self.decided_nums:
                possible_cells = []
                for cell in self.cells:
                    if not cell.finished and i in cell.available:
                        possible_cells.append(cell)
                if len(possible_cells) == 1:
                    possible_cells[0].available = [i]
