import tkinter as tk
import tkinter.font as tkfont


class Gui:

    def __init__(self, parent, solver):
        self.root = parent
        self.font = tkfont.Font(family='Calibri', size=14, weight='bold')
        self.canvas = tk.Canvas(self.root, width=990, height=990)
        self.canvas.grid(columnspan=11, rowspan=11)
        self.canvas.configure(background='white')
        self.solver = solver
        self.entries = []

    def __get_user_input(self):
        for i in range(9):
            for j in range(9):
                new_value = self.entries[i][j].get()
                new_value = 0 if new_value == '' else int(new_value)
                if new_value not in range(0,10):
                    raise ValueError('Encountered invalid value')
                self.solver.sudoku.rows[i][j] = new_value

    def __solve(self):
        try:
            self.__get_user_input()
        except ValueError as e:
            self.__draw_solve_button(str(e))
            return
        if self.solver.sudoku.is_not_valid():
            self.__draw_solve_button('This is not a valid Sudoku')
            return
        self.solver.solve()
        if self.solver.found_one_solution:
            self.__draw_solve_button('Solved')
        else:
            self.__draw_solve_button('Could not find a solution')
        self.__draw_entries()

    def __draw_solve_button(self, message='Solve'):
        button_text = tk.StringVar()
        button_text.set(message)
        solve_button = tk.Button(self.root,
                                 textvariable=button_text,
                                 font=self.font,
                                 command=lambda:self.__solve(),
                                 height = 2,
                                 width = 108,
                                 borderwidth=0,
                                 background='green')
        solve_button.place(x=-2, y=950)

    def __draw_entries(self):
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                value = self.solver.solution.rows[i][j]
                box_text = tk.StringVar()
                box_text.set('' if value == 0 else value)
                box_state = 'normal' if value == 0 else 'disabled'
                box = tk.Entry(self.root,
                               state=box_state,
                               textvariable=box_text,
                               font=self.font,
                               justify='center',
                               width=5,
                               borderwidth=0,
                               background='white')
                box.grid(row=i+1, column=j+1, ipadx=2, ipady=10)
                row.append(box)
            self.entries.append(row)

    def __draw_lines(self):
        x_0, y_0 = 60, 60
        x_1, y_1 = 350, 350
        x_2, y_2 = 640, 640
        x_3, y_3 = 930, 930

        self.canvas.create_line(x_0, y_0, x_0, y_3)
        self.canvas.create_line(x_1, y_0, x_1, y_3)
        self.canvas.create_line(x_2, y_0, x_2, y_3)
        self.canvas.create_line(x_3, y_0, x_3, y_3)

        self.canvas.create_line(x_0, y_0, x_3, y_0)
        self.canvas.create_line(x_0, y_1, x_3, y_1)
        self.canvas.create_line(x_0, y_2, x_3, y_2)
        self.canvas.create_line(x_0, y_3, x_3, y_3)

    def display(self):
        self.__draw_lines()
        self.__draw_entries()
        self.__draw_solve_button()
