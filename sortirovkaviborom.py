# исходный список
numbers = [29, 10, 14, 37, 13]
# сортировка выбором (selection sort)
n = len(numbers)
for i in range(n - 1):
    # поиск минимального элемента в неотсортированной части
    min_idx = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    # обмен элементами
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    # вывод состояния списка после прохода
    print(numbers)