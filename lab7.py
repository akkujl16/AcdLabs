def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Уменьшение зазора на каждой итерации
    while gap > 0:
        # Сортировка вставками для элементов с текущим зазором
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Сдвиг элементов, пока не найдется правильное место для temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Исходный массив:", numbers)
sorted_numbers = shell_sort(numbers)
print("Отсортированный массив:", sorted_numbers)
