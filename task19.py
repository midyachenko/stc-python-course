#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.

zadacha = input("Введите задачу: ")
zadacha_list = zadacha.split(" ")
a = int(zadacha_list[0])
b = int(zadacha_list[2])
znak = zadacha_list [1]
match znak:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)