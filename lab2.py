import re

def calculate_expression(expr: str):
    # Проверка на наличие знака "=" строго в конце
    expr = expr.strip()
    if not expr.endswith('='):
        return "Ошибка: выражение должно заканчиваться знаком '='"
    
    # Удаление '=' для дальнейшего вычисления
    base_expr = expr[:-1].replace(" ", "")
    if not base_expr:
        return "Ошибка: пустое выражение"

    # Проверка на недопустимые символы
    # Разрешены только цифры, точки, знаки +, -, *, /, ( и )
    if not re.match(r'^[0-9.+\-*/()]+$', base_expr):
        return "Ошибка: выражение содержит недопустимые символы"

    # Проверка синтаксиса (подряд идущие операторы, знаки в конце и т.д.)
    # Например: ++, *-, /+, оператор перед закрывающей скобкой или в конце строки
    if re.search(r'[+\-*/]{2,}', base_expr):
        return "Ошибка: два оператора не могут идти подряд"
    if re.search(r'[+\-*/]$', base_expr):
        return "Ошибка: выражение не может заканчиваться оператором"
    if re.search(r'\([+\*/]', base_expr):  # (-5 разрешен, а (+5 или (*5 нет
        return "Ошибка: некорректный оператор после открывающей скобки"
    if re.search(r'[+\-*/]\)', base_expr):
        return "Ошибка: оператор перед закрывающей скобкой"
    if re.search(r'\(\)', base_expr):
        return "Ошибка: пустые скобки"

    # Проверка баланса скобок
    bracket_balance = 0
    for char in base_expr:
        if char == '(':
            bracket_balance += 1
        elif char == ')':
            bracket_balance -= 1
        if bracket_balance < 0:
            return "Ошибка: нарушен баланс скобок (лишняя закрывающая скобка)"
    
    if bracket_balance != 0:
        return "Ошибка: не все открытые скобки закрыты"

    # Проверка на деление на ноль
    # Поиск символа '/' после которого идет ноль, не являющийся частью другого числа
    if re.search(r'\/0+(?!\.\d*[1-9])(?!\d)', base_expr):
        return "Ошибка: деление на ноль"

    # Вычисление результата с перехватом непредвиденных ошибок деления
    try:
        result = eval(base_expr)
        return f"Результат: {result}"
    except ZeroDivisionError:
        return "Ошибка: деление на ноль во время вычислений"
    except Exception as e:
        return f"Ошибка при вычислении выражения"

user_input = input("Введите математическое выражение (например, 2+7*(3/9)-5=): ")
print(calculate_expression(user_input))
