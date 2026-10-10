class SimpleCalculator:
    def __init__(self, expr):
        self.expr = expr.replace(" ", "").rstrip("=") # удаление пробелов и знака '=' с конца
        self.pos = 0 # индекс обрабатываемого символа
        self.check_brackets() # метод проверки скобок

    def check_brackets(self):
        balance = 0
        for char in self.expr:
            if char == '(': balance += 1
            elif char == ')': balance -= 1
            if balance < 0:
                raise ValueError("Ошибка: Лишняя закрывающая скобка")
        if balance != 0:
            raise ValueError("Ошибка: Не все скобки закрыты")

    def eval(self): # разбор текста
        result = self.eval_expression()
        if self.pos < len(self.expr): # проверка дошел ли курсор до конца т.е отработали ли все функции
            raise ValueError(f"Ошибка: Некорректный символ '{self.expr[self.pos]}'") # индекс курсора в строке
        return result

    def eval_expression(self): # обработка +-
        a = self.eval_term()
        while self.pos < len(self.expr) and self.expr[self.pos] in ('+', '-'):
            oper = self.expr[self.pos]
            self.pos += 1
            b = self.eval_term()
            a = a + b if oper == '+' else a - b
        return a

    def eval_term(self): # обработка *:
        a = self.eval_factor()
        while self.pos < len(self.expr) and self.expr[self.pos] in ('*', '/'):
            oper = self.expr[self.pos]
            self.pos += 1
            b = self.eval_factor()
            if oper == '*':
                a *= b
            else:
                if abs(b) < 0.000000001:
                    raise ZeroDivisionError("Ошибка: Деление на ноль")
                a /= b
        return a

    def eval_factor(self): # обработка чисел, скобок, унарного минуса и плюса
        if self.pos >= len(self.expr):
            raise ValueError("Ошибка: Неполное выражение")

        # унарный минус
        if self.expr[self.pos] == '-':
            self.pos += 1
            return -self.eval_factor()
        
        # унарный плюс
        if self.expr[self.pos] == '+':
            self.pos += 1
            return self.eval_factor()

        # выражение в скобках
        if self.expr[self.pos] == '(':
            self.pos += 1  
            result = self.eval_expression()
            if self.pos >= len(self.expr) or self.expr[self.pos] != ')':
                raise ValueError("Ошибка: Нет закрывающийся скобки")
            self.pos += 1 
            return result

        # считывание числа
        start = self.pos # начало блока
        while self.pos < len(self.expr) and (self.expr[self.pos].isdigit() or self.expr[self.pos] == '.'):
            self.pos += 1
        piece = self.expr[start:self.pos] # создание блока от начала до индекса который не число
        if not piece:
            raise ValueError(f"Ошибка: Нет числа в позиции {start}")       
        try:
            return float(piece)
        except ValueError:
            raise ValueError(f"Ошибка: Неверный формат числа '{piece}'")

text = input("Введите выражение (2+7*(3/9)-5=): ")
try:
    calc = SimpleCalculator(text)
    res = calc.eval()
    print("Результат:", int(res) if res.is_integer() else res)
except (ValueError, ZeroDivisionError) as e:
    print(e)
