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

    def is_not_valid(self):
        units = flatten([self.rows, self.columns, self.fields])
        for unit in units:
            if len([v for v in unit if v != 0]) != len(set(unit) - set([0])):
                return True
        return False

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
