# Считываем список урожайностей
a = list(map(int, input().split()))

n = len(a)
max_harvest = 0

# Перебираем все кусты
for i in range(n):
    # Вычисляем индексы двух соседних кустов
    left = (i - 1 + n) % n
    right = (i + 1) % n

    # Вычисляем, сколько ягод может собрать собирающий модуль
    harvest = a[i] + a[left] + a[right]

    # Обновляем максимальное значение
    max_harvest = max(max_harvest, harvest)

# Выводим ответ
print(max_harvest)