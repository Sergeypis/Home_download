""" Программа - генератор случайных паролей"""

import string


def initial_data() -> (int, list):
    """
    Функция производит валидацию введенного значения пользователем
    """
    print("Добро пожаловать в программу по генерации случайных паролей!")
    print("." * 60)
    
    while True:
        password_len = input("Введите длину желаемого пароля более 5 символов: ")
        if not password_len.isdigit():
            print("Нужно ввести только целое число!!!")
            continue
        
        if int(password_len) < 6:
            print("Пароль должен быть более 5 символов!!!")
            continue
        password_len = int(password_len)
        break
    print("-" * 60)
    print(f"Будет сгенерирован пароль из '{password_len}' символов.")
    print("-" * 60)
    
    spec_symbols = input("Введите спецсимволы, если их нужно использовать в пароле. Иначе нажмите Enter: ")    
        if spec_symbols
    return password_len
