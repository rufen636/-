try:
    print("Введите а")
    a = int(input())
    print("Введите b")
    b = int(input())
    c = a / b
except Exception as e:
    print(e)
else:
    print(f"Результат:{c}")
    print("всё хорошо,деления на 0 не обнаружено")
finally:
    print("Awesome!")
