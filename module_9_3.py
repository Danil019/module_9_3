first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин
first_result = (abs(len(s1) - len(s2)) for s1, s2 in zip(first, second) if len(s1) != len(s2))

# Генераторная сборка для сравнения длин
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результата
print(list(first_result))
print(list(second_result))