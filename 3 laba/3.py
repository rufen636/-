import re

# Создаем текстовый файл с описанием учебных предметов
with open("учебные_предметы.txt", "w") as file:
    file.write("Информатика: 100(л) 50(пр) 20(лаб)\n")
    file.write("Физика: 30(л) 10(лаб)\n")
    file.write("Физкультура: 30(пр)\n")

# Инициализируем пустой словарь для хранения данных
predmeti = {}

# Считываем данные из файла
with open("учебные_предметы.txt", "r") as file:
    lines = file.readlines()

# Обходим каждую строку файла
for line in lines:
    parts = line.strip().split(
        ":"
    )  # Разделяем строку на название предмета и его описание
    predmet = parts[0]  # Название предмета
    description = parts[1]  # Описание занятий

    # Используем регулярное выражение для поиска чисел в описании занятий
    quantity = re.findall(r"\d+", description)

    # Считаем сумму чисел в описании
    general_quantity = sum(map(int, quantity))

    # Добавляем предмет и его общее количество занятий в словарь
    predmeti[predmet] = general_quantity

# Выводим полученный словарь на экран
print("Словарь учебных предметов и их общего количества занятий:")
print(predmeti)
