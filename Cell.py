class Cell:

    def __init__(self, num):
        self.num = num
        self.finished = num != 0
        self.available = []
        self.box = None
        self.column = None
        self.row = None
        if num == 0:
            self.available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.available = [num]

    def step(self):
        if not self.finished:
            if len(self.available) == 1:
                self.num = self.available[0]
                self.finished = True
        return self.finished

    def __str__(self):
        return str(self.num)
