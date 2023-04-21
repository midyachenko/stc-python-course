# todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря. Каждая буква сдвигается на заданное число n позиций вправо. Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.


def code(string, n):
    encrypted = ""
    for c in string:
        if c.isupper():  # проверить, является буква заглавной
            c_index = ord(c) - ord('A')
            # сдвиг  на n
            c_shifted = (c_index + n) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + n) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # если это цифра, сдвинуть на n
            c_new = (int(c) + n) % 10
            encrypted += str(c_new)
        else:
            # если не буква и не цифра не меняем
            encrypted += c
    return encrypted


string = input("Введите строку на английском языке: ")
n = int(input("Введите n: "))
print(code(string, n))
