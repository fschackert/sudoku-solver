"""Sudoku Solver"""

def flatten(list2d):
    return [item for list1d in list2d for item in list1d]


class Sudoku:

    def __init__(self, rows):
        self.rows = rows

    @property
    def columns(self):
        return [self.flat[i::9] for i in range(9)]

    @property
    def fields(self):
        fields = []
        for i in range(0, 9, 3):
            for j in range(3):
                field = []
                for k in range(3):
                    field.append(self.flat[(i+k)*9:(i+k+1)*9][j*3:(j+1)*3])
                fields.append(flatten(field))
        return fields

    @property
    def flat(self):
        return flatten(self.rows)

    def __str__(self):
        flat = self.flat
        out = '-------------------------\n'
        for i in range(81):
            if i%3 == 0:
                out += '| '
            if flat[i] == 0:
                out += '  '
            else:
                out += str(flat[i]) + ' '
            if (i+1)%9 == 0:
                out += '| \n'
            if (i+1)%27 == 0:
                out += '-------------------------\n'
        return out


class Solver:

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.all_values = set(range(1, 10))

    def __possible_values(self, i, j):
        used_values = set(self.sudoku.rows[i])
        used_values |= set(self.sudoku.columns[j])
        used_values |= set(self.sudoku.fields[i//3*3+j//3])
        return self.all_values - used_values

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.sudoku.rows[i][j] != 0:
                    continue
                for value in self.__possible_values(i, j):
                    self.sudoku.rows[i][j] = value
                    self.solve()
                    self.sudoku.rows[i][j] = 0
                return
        print(self.sudoku)


if __name__ == '__main__':

    EXAMPLE = [[0, 3, 4, 7, 5, 2, 0, 0, 0],
               [6, 0, 0, 0, 0, 0, 7, 0, 0],
               [0, 0, 0, 3, 0, 0, 0, 0, 5],
               [5, 0, 2, 4, 0, 0, 8, 0, 0],
               [0, 8, 0, 0, 0, 0, 2, 0, 0],
               [0, 0, 9, 0, 2, 8, 4, 0, 0],
               [1, 0, 0, 8, 4, 0, 0, 0, 0],
               [0, 4, 0, 0, 0, 0, 0, 9, 0],
               [2, 7, 0, 0, 9, 0, 6, 1, 0]]

    SUDOKU = Sudoku(EXAMPLE)
    SOLVER = Solver(SUDOKU)
    SOLVER.solve()
