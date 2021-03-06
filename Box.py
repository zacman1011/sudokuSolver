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
                cell.available = [num for num in cell.available if num not in cell.decided_nums]
