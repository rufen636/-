def prostoe(data):
    if data <= 1:
        return "число не простое"
    for i in range(2, int(data)):
        if data % i == 0:
            return "число составное"
    return "число простое"


res = prostoe(12)
print(res)
