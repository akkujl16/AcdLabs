def heapify(arr, n, i):
    largest = i          # наибольший элемент как корень
    left = 2 * i + 1     # левый элемент
    right = 2 * i + 2    # правый элемент

    # левый элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # правый элемент больше, чем самый большой элемент на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # самый большой элемент не корень, обмен местами
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest) # рекурсивная перестройка затронутого поддерева


def heap_sort(arr):
    n = len(arr)

    # строительство max-heap, начало с последнего узла, у которого есть дети, и движение вверх к корню
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # последовательное извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # перемещение максимального элемента в конец массива
        heapify(arr, i, 0) # heapify на уменьшенной куче, чтобы восстановить порядок
    return arr
  
numbers = [12, 11, 13, 5, 6, 7, -3, 0, 25, 4]
print("Исходная последовательность: ", numbers)
sorted_numbers = heap_sort(numbers.copy())
print("Отсортированная последовательность:", sorted_numbers)
