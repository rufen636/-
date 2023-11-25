try:
    f1 = open(r"/Users/ruslansamojlov/Desktop/сяп/3 laba/F1.txt", "w")
    f2 = open(r"/Users/ruslansamojlov/Desktop/сяп/3 laba/F2.txt", "w")
except FileNotFoundError as e:
    print(e)
finally:
    print("Файл успешно открыт!:)")
print("Введите данные, которые хотите записать в файл")
while True:
    g = input()
    if not g:  #  если ничего не ввожу
        break
    f1.write(g + "\n")

f1 = open(r"/Users/ruslansamojlov/Desktop/сяп/3 laba/F1.txt", "r")
for line in f1:
    if line[0].isdigit():
        f2.write(line)

f2 = open(r"/Users/ruslansamojlov/Desktop/сяп/3 laba/F2.txt", "r")
line1 = f2.readline()
word_count = len(line1.split())
print(f"кол-во слов в первой строке:{word_count}")
f1.close()
f2.close()
