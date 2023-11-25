def process_input(data):
    if isinstance(data, list):

        def remove_duplicates(input_list1):
            unique_data = []

            for item in input_list1:
                if item not in unique_data:
                    unique_data.append(item)

            return unique_data

        unique_data1 = remove_duplicates(input_list)
        sum_after_positive = 0
        positive_found = False
        for item in unique_data1:
            if item > 0 and not positive_found:
                positive_found = True
            elif positive_found:
                sum_after_positive += item
        return sum_after_positive

    elif isinstance(data, dict):
        sorted_dict = {
            k: v
            for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)
        }
        return sorted_dict

    elif isinstance(data, int):
        if data <= 1:
            return "Число не является простым."
        for i in range(2, int(data)):
            if data % i == 0:
                return "Число не является простым."
        return "Число является простым."

    elif isinstance(data, str):
        unicode_list = [ord(char) for char in data]
        return unicode_list

    else:
        return "Тип данных не поддерживается."


input_list = [-2, 3, 2, 4, 5, 7, 4, 5, 6]
input_dict = {"a": 3, "b": 1, "c": 2}
input_number = 18
input_string = "Hello, World!"


result_list = process_input(input_list)
result_dict = process_input(input_dict)
result_number = process_input(input_number)
result_string = process_input(input_string)

print("Результат для списка:", result_list)
print("Результат для словаря:", result_dict)
print("Результат для числа:", result_number)
print("Результат для строки:", result_string)
