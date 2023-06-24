# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять cуществующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Table:
    def __init__(self, colnames: list):
        self.colnames = colnames
        self.rows = []

    def add_row(self, row: dict):
        if any(colname not in tuple(row) for colname in self.colnames):  # хотя бы один элемент не соответствует
            print('Такой колонки нет')
        else:
            self.rows.append(row)

    def get_column(self, colname):
        if (colname not in self.colnames):
            print('Такой колонки нет')
        return [r[colname] for r in self.rows]


    def sum(self, colname: str):
        if colname not in self.colnames:
          print('Неправильный формат')
        return sum([r[colname] for r in self.rows])



table1 = Table([1, 2])
table1.add_row({1: 5, 2: 7})
table1.add_row({1: 3, 2: 9})
table1.add_row({1: 1, 2: 6})
table1.add_row({1: 4, 2: 8})
print(table1.get_column(1))
print(table1.get_column(2))
print(table1.rows)