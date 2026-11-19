# Ввод количества элементов
n = int(input("Введите N (1-800): "))
# Ввод списка целых чисел
numbers = []

for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    numbers.append(num)

# Преобразование элементов списка по правилам 
transformed = []
for x in numbers:
    if x > 0 and x % 2 == 0:
        transformed.append(x ** 2)
    elif x % 2 != 0:
        if x < 0:
            transformed.append(abs(x))
        else:
            transformed.append(x * 3)
    elif x < 0:
        transformed.append(abs(x))
    else:
        transformed.append(0)

# Удаление всех кратных чисел, кратных 5
filtred = [x for x in transformed if x % 5 != 0]

# Обработка результатов и краевх случаев 
if len(filtred) == 0:
    print("После фильтрации список оказался пустым.")
else:
    total_sum = sum(filtred)
    average = total_sum / len(filtred)
    minimum = min(filtred)
    maximum = max(filtred)
    above_avg_count = len([x for x in filtred if x > average])

    print(f"Сумма: {total_sum}")
    print(f"Среднее: {average}")
    print(f"Минимальное: {minimum}")
    print(f"Максимальное: {maximum}")
    print(f"Количество элементов больше среднего: {above_avg_count}")

    # Сортировка по возрастанию
    sorted_list = sorted(filtred)
    print(f"Отсортированный список: {sorted_list}")

    # Поиск второго по величине элемента
    unique_sorted = sorted(set(filtred))
    if len(unique_sorted) < 2:
        print("Второго по величине элемента не существует.")
    else:
        print(f"Второй по величине элемент: {unique_sorted[-2]}")
