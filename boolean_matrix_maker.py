
class BooleanMatrix:
    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        self.matrix = [[0 for x in range(self.columns)]for y in range(self.rows)]

    def __str__(self):
        return str(self.matrix)

    def draw_horizontal(self, row: int, columns: list):
        for i in columns:
            self.matrix[row - 1][i - 1] = 1

    def draw_vertical(self, column: int, rows: list):
        for i in rows:
            self.matrix[i - 1][column - 1] = 1
