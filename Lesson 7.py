#Задание 1
class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][idx] + other.value[row][idx]
                    for idx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Ошибка - Матрицы разного размера")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )


a = Matrix([
    [11, 12, 13],
    [14, 15, 16],
])

b = Matrix([
    [21, 22, 23],
    [24, 25, 26],
])

c = a + b

print(c)



# Задание 2
# class Textil:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_square_c(self):
#         return self.width / 6.5 + 0.5
#
#     def get_square_j(self):
#         return self.height * 2 + 0.3
#
#     @property
#     def get_sq_full(self):
#         return str(f'Площадь общая ткани \n'
#                    f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')
#
# class Coat(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_c = round(self.width / 6.5 + 0.5)
#
#     def __str__(self):
#         return f'Площадь на пальто {self.square_c}'
#
# class Jacket(Textil):
#     def __init__(self, width, height):
#         super().__init__(width, height)
#         self.square_j = round(self.height * 2 + 0.3)
#
#     def __str__(self):
#         return f'Площадь на костюм {self.square_j}'
#
# coat = Coat(2, 4)
# jacket = Jacket(1, 2)
# print(coat)
# print(jacket)
# print(coat.get_sq_full)
# print(jacket.get_sq_full)
# print(jacket.get_square_c())
# print(jacket.get_square_j())


# Задание 3
class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)
        #self.result = result

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        # self.result = Cell(self.quantity + other.quantity)
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        '''
        Выдает ошибку о том, что результат не число  при вычислении
        if int(Cell(self.quantity - other.quantity)) > 0:
            return Cell(int(self.quantity - other.quantity))
        else:
            return f'Операция вычитания невозможна'""
        '''
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

        # return Cell(int(self.quantity - other.quantity))

    def __mul__(self, other):
        #self.result = Cell(int(self.quantity * other.quantity))
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        #self.result = Cell(round(self.quantity // other.quantity))
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(9)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)