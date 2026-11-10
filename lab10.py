def merge_sort(arr):
    # отсортированный массив
    if len(arr) <= 1:
        return arr

    # середина массива и деление на две части
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # слияние отсортированных половин
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    # сравнивнение элементов из левой и правой половин и добавление меньшего в результат
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавление оставшихся элементов (один из списков закончился раньше)
    result.extend(left[i:])
    result.extend(right[j:])
    return result

numbers = [38, 27, 43, 3, 9, 82, 10, -5, 0]
print("Исходная последовательность:", numbers)

sorted_numbers = merge_sort(numbers)
print("Отсортированная последовательность:", sorted_numbers)
