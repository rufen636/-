ma = [[-1, -2, -3], [4, -5, 6], [-7, -8, -9]]


def find_first_negative_row(ma):
    for row in ma:
        if all(element < 0 for element in row):
            return row
    return None


def sum_row_elements(row):
    if row is None:
        return 0
    return sum(row)


negative_row = find_first_negative_row(ma)
if negative_row:
    row_sum = sum_row_elements(negative_row)
    print(f"Элементы матрицы:{ma}")
    print("Первая строка, все элементы которой отрицательны:", negative_row)
    print("Сумма элементов этой строки:", row_sum)
else:
    print("В матрице нет строк, все элементы которых отрицательны.")
