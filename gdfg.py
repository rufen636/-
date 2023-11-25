ma = [[-2,-3,-1],[2,4,-2],[1,6,5]]
def find_first_negative_row(ma):
    for row in ma :
        if all(element<0 for element in row ):
           return row
    return None      

def sum_row_elements(row):
    if row == None:
        return 0 
    return sum(row)

negative_row=find_first_negative_row(ma)
if negative_row:
    row_sum = sum_row_elements(negative_row)
    print(f"Первая строка,все элементы которой отрицательны:{negative_row}")
    print(f"Сумма элементов этой строки:{row_sum}")
else:
    print("В метрице нет строк, все элементы которой отрицательны")