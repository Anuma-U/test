def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return [result, incorrect_data]

def calculate_average(numbers):
    number = numbers
    error = 0
    integer = []
    try:
        for num in number:
            try:
                if isinstance(num, int):
                    integer.append(num)
                else:
                    error += num
            except TypeError:
                print(f"Некорректный тип данных для подсчёта суммы - {num}")
    except TypeError:
        print(f"Некорректный тип данных для подсчёта суммы")
        return None
    try:
        sr_znach = personal_sum(integer)[0]/len(integer)
    except ZeroDivisionError:
        return 0
    return sr_znach

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
