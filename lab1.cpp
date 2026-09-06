#include <iostream>
#include <string>
#include <stack>

// Функция для проверки правильности скобочной последовательности
bool correctChainOfBrackets(const std::string& str) {
    std::stack<char> stackOpenBrackets;

    for (char ch : str) {
        // Если скобка открывающаяся, то кладем её в стек
        if (ch == '(' || ch == '{' || ch == '[') {
            stackOpenBrackets.push(ch);
        }
        // Если скобка закрывающаяся, проверяем стек
        else if (ch == ')' || ch == '}' || ch == ']') {
            // Если стек пуст, значит для закрывающей скобки нет открывающей
            if (stackOpenBrackets.empty()) {
                return false;
            }

            char top = stackOpenBrackets.top();
            // Проверка, соответствует ли тип закрывающей скобки типу открывающей на вершине стека
            if ((ch == ')' && top == '(') ||
                (ch == '}' && top == '{') ||
                (ch == ']' && top == '[')) {
                stackOpenBrackets.pop(); // Соответствие найдено, убирание из стека
            }
            else {
                return false; // Типы скобок не совпали
            }
        }
        // Игнорирование другич символов
    }

    // Если стек пустой, значит все скобки закрылись правильно
    return stackOpenBrackets.empty();
}

int main() {
    std::setlocale(LC_ALL, "Russian");

    std::string input;
    std::cout << "Введите скобочную строку: ";
    std::cin >> input;

    // Проверка на пустой ввод
    if (input.empty()) {
        std::cout << "Строка пустая" << std::endl;
        return 0;
    }

    if (correctChainOfBrackets(input)) {
        std::cout << "Строка существует" << std::endl;
    }
    else {
        std::cout << "Строка не существует" << std::endl;
    }
    return 0;
}
