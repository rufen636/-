my_dict = {"a": 111, "b": 122, "c": 566, "d": 405, "e": 21, "f": 266}


sorted_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)


for i in range(3):
    print(sorted_dict[i][0])
