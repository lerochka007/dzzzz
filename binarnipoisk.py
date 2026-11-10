# отсортированный список и целевое число
numbers = [2, 5, 8, 11, 14, 18, 21, 25, 30]
x = 18
# границы поиска
left = 0
right = len(numbers) - 1
index = -1
# бинарный поиск
while left <= right:
    mid = (left + right) // 2
    if numbers[mid] == x:
        index = mid
        break
    elif numbers[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
print(index)