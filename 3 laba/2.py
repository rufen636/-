try:
    f1 = open(r"/Users/ruslansamojlov/Desktop/сяп/3 laba/Kinoteatr.txt", "r")
except FileNotFoundError as e:
    print(e)
finally:
    print("Файл успешно открыт!:)")


def menu():
    while True:
        print("1)Фильмы < 15\n2)Фильмы по дате")
        try:
            unit = int(input("Введите выбор:"))
        except Exception as e:
            print(e)
        if unit == 1:
            lines = f1.readlines()
            for line in lines:
                partw = line.split()
                title = partw[0]
                price = float(partw[2])
                if price < 15:
                    print(f"Ниже 15 рублей:{title} {price}")
        if unit == 2:
            lines = f1.readlines()
            date_to_filter = str(
                input("Введите дату для поиска фильмов (в формате дд.мм.гггг): ")
            )
            print(f"Фильмы на {date_to_filter}:")
            for line in lines:
                partw = line.split()
                date = str(partw[1])
                if date == date_to_filter:
                    title = partw[0]
                    print(title)
        if unit == 3:
            break


menu()
f1.close()
