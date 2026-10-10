def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1): # до предпоследнего так как он уже будет максимальным
        # поиск индекса минимального элемента в неотсортированной части
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # обмен местами найденного минимального элемента с текущим
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

numbers = [64, 25, 12, 22, 11]   
print("Исходный массив:", numbers)
selection_sort(numbers)
print("Отсортированный массив:", numbers)
