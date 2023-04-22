# Вводим первый список чисел
list1 = list(map(int, input("Введите первый список чисел через пробел: ").split()))

# Вводим второй список чисел
list2 = list(map(int, input("Введите второй список чисел через пробел: ").split()))

# Создаем множества из списков
set1 = set(list1)
set2 = set(list2)

# Находим пересечение множеств
result_set = set1 & set2

# Преобразуем множество в список и сортируем его
result_list = sorted(list(result_set))

# Выводим результат
print(result_list)