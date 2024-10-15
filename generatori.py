first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (abs(len(i) - len(j)) for i, j in zip(first, second) if len(i) != len(j))
print(list(first_result))
second_result = (len(first[i]) == len(second[j]) for i in range(len(first)) for j in range(i, len(second)) if i == j)
print(list(second_result))