def calculator():
    x = float(input("Введите первое число: "))
    op = input("Введите операцию (+, -, *, /): ")
    y = float(input("Введите второе число: "))

    if op == '+':
        print(f"Результат: {x + y}")
    elif op == '-':
        print(f"Результат: {x - y}")
    elif op == '*':
        print(f"Результат: {x * y}")
    elif op == '/':
        print("Ошибка: деление на ноль!" if y == 0 else f"Результат: {x / y}")
    else:
        print("Некорректная операция.")

if __name__ == "__main__":
    calculator()
