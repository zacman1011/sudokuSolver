class Line:

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

    def __str__(self):
        output = ""
        count = 0
        for cell in self.cells:
            output += str(cell)
        return output
