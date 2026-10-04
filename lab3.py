def numbs(x):
    if x < 1:
        return []

    result = []
    
    # Внешний цикл по степеням тройки
    p3 = 1
    while p3 <= x:
        # Второй цикл по степеням пятёрки
        p5 = 1
        while p3 * p5 <= x:
            # Внутренний цикл по степеням семёрки
            p7 = 1
            while p3 * p5 * p7 <= x:
                # Добавление найденного числа в список
                result.append(p3 * p5 * p7)
                p7 *= 7
            p5 *= 5
        p3 *= 3

    # Сортировка списка по возрастанию
    result.sort()
    return result

try:
    user_input = int(input("Введите число x: "))
        
    numbers = numbs(user_input)
        
    print(f"Числа от 1 до {user_input}, удовлетворяющие условию:")
    print(numbers)
        
except ValueError:
    print("Введите корректное целое число")
