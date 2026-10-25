def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # выходной массив для отсортированных чисел
    count = [0] * 10  # массив для подсчета цифр от 0 до 9

    # количество вхождений каждой цифры в текущем разряде
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # count[i] указывает на реальную позицию этой цифры в выходном массиве
    for i in range(1, 10):
        count[i] += count[i - 1]

    # выходной массив, движение с конца для сохранения стабильности
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # копирование отсортированных по разряду числа обратно в массив arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    # максимальное число для максимального количества разрядов
    max_num = max(arr)

    # проход по всем разрядам
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

numbers = [170, 45, 75, 90, 802, 24, 2, 66]
print("Исходный список:", numbers)
sorted_numbers = radix_sort(numbers)
print("Отсортированный список:", sorted_numbers)
