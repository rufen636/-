# ADD
# e = [1, 2]
# e.insert(1, 3)  # добавление элемента в список
# print(e)

#  замена
# g = [1, 2]
# g[1] = 3
# print(g)

# удалени
# h = [1, 5, 3, 'h']
# del h[1]  # удаление но индаксу
# print(h)
# h.remove('h')  # по элементу
# print(h)

# elements = [1, 3, 6, 'a', 'b', 'abc', 123, 435]
# del elements[4:]  # после 4 включительно
# print(elements)
# del elements[:2]  # до 2
# print(elements)
# del elements[1:3]  # от 1 до 3   (первый индекс всегда включительно а второй нет )
# print(elements)

# проверка на наличие элемента, оператор  in
# e = [1, 3, 'n', 4]
# if 'b' in e:
#    print('yes')   #else:
#    print('no')

# Объединение списков
# a = [1]
# b = [2, 5]
# print(a+b)

# d = [4, 7, 2]
# e = ['hello', ' world']
# e.extend(d) # не возвращает новый список а дополняет текущий
# print(e)

# Копирование
# elements.copy() – встроенный метод copy (доступен с Python 3.3);
# 2.list(elements) – через встроенную функцию list() ;
# 3.copy.copy(elements) – функция copy() из пакета copy;
# 4.elements[:] – через создание среза (устаревший синтаксис);
# import copy
# a = ["кот", "слон", "змея"]
# b = a.copy()
# print(a, b)
# d = list(a)
# print(a, d)
# e = copy.copy(a)
# print(a, e)
# f = copy.deepcopy(a)
# print(a, f)
# c = a[:]  # устаревший синтаксис
# print(a, c)

# Циклы
# f = [1, 2, 3, 4, 5]
# for i in f:
#    print(i)

# Методы
# list.append(x) – позволяет добавлять элемент в конец списка;
# list1.extend(list2) – предназначен для сложения списков;
# list.insert(i, x) – служит для добавления элемента на указанную
# позицию( i – позиция, x – элемент);
# list.remove(x) – удаляет элемент из списка (только первое вхождение);
# list.clear() – предназначен для удаления всех элементов (после этой
# операции список становится пустым []);
# list.copy() – служит для копирования списков.
# list.count(x) – посчитает количество элементов x в списке;
# ist.index(x) – вернет позицию первого найденного элемента x в списке;
# list.pop(i) - удалит элемент из позиции i ;
# list.reverse() – меняет порядок элементов в списке на противоположный;
# list.sort() – сортирует список;

# СОРТИРОВКА
# sort (по возрастанию)
# elements = [3, 19, 0, 3, 102, 3, 1]
# elements.sort()
# print(elements)
# sort (по убыванию)
# elements = [3, 19, 0, 3, 102, 3, 1]
# elements.sort(reverse=True)
# print(elements)

# evens = [i for i in range(21) if i % 2 == 0]
# print(evens)

# Создать словарь
# d_1 = {}
# d = dict (short='dict', long='dictionary')
# d_2 = dict([(1, 1), (2, 4)])
# print (d, '\n', d-2)

# dict.clear() - очищает словарь.
# dict.copy() - возвращает копию словаря.
# dict.items() - возвращает пары (ключ, значение).
# dict.keys() - возвращает ключи в словаре.
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# dict.values() - возвращает значения в словаре.
# стандартный метод len(dict) – определяет количество элементов в списке.

# Удаление словаря
# del D[key]
# D - заданный словарь
# key  ключ

person = dict(zip(['bmw', 'tesla'], [['m3', 'm5', 'm7'], ['y', 'c', 'r']]))
print(person['bmw'][0], person['bmw'][2])
print(person['tesla'][0], person['tesla'][2])
