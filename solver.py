from sudoku import Sudoku


class Solver:

    def __init__(self, given_values):
        self.sudoku = Sudoku(given_values)
        self.solution = Sudoku(self.sudoku.rows)
        self.found_one_solution = False
        self.__all_values = set(range(1, 10))

    def __possible_values(self, i, j):
        used_values = set(self.sudoku.rows[i])
        used_values |= set(self.sudoku.columns[j])
        used_values |= set(self.sudoku.fields[i//3*3+j//3])
        return self.__all_values - used_values

    def solve(self):
        if self.found_one_solution:
            return
        for i in range(9):
            for j in range(9):
                if self.sudoku.rows[i][j] != 0:
                    continue
                for value in self.__possible_values(i, j):
                    self.sudoku.rows[i][j] = value
                    self.solve()
                    self.sudoku.rows[i][j] = 0
                return
        self.solution = Sudoku([[value for value in row] for row in self.sudoku.rows])
        self.found_one_solution = True
