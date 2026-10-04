#include <iostream>
#include <vector>

// Метод прочёсывания
void combSort(std::vector<int>& arr) {
    size_t n = arr.size();
    size_t gap = n;
    const double shrink = 1.3;
    bool swapped = true;

    while (gap > 1 || swapped) {
        gap = static_cast<size_t>(gap / shrink);
        if (gap < 1) {
            gap = 1;
        }

        swapped = false;

        // Сравнивание элементов на расстоянии gap
        for (size_t i = 0; i < n - gap; ++i) {
            if (arr[i] > arr[i + gap]) {
                std::swap(arr[i], arr[i + gap]);
                swapped = true;
            }
        }
    }
}

// Сортировка вставками
void insertionSort(std::vector<int>& arr) {
    size_t n = arr.size();
    for (size_t i = 1; i < n; ++i) {
        int key = arr[i];
        int j = static_cast<int>(i) - 1;

        // Передвижение элементов, которые больше ключа, на одну позицию вперёд
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Функция для вывода вектора на экран
void printArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}

int main() {
    std::setlocale(LC_ALL, "Russian");
    // Исходная последовательность чисел
    std::vector<int> sourceArr = { 34, -2, 10, -9, 0, 78, 15, 6, 2, 100, -5 };

    std::cout << "Исходный массив: ";
    printArray(sourceArr);

    // Тестирование метода 1
    std::vector<int> arr1 = sourceArr;
    combSort(arr1);
    std::cout << "После сортировки прочёсыванием: ";
    printArray(arr1);

    // Тестирование метода 2
    std::vector<int> arr2 = sourceArr;
    insertionSort(arr2);
    std::cout << "После сортировки вставками: ";
    printArray(arr2);

    return 0;
}
