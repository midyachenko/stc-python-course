# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.

x = (input("Введите число X "))
y = (input("Введите число Y "))
z = (input("Введите число Z "))
list = [x, y, z]
print(list)
print("Ответ: Наибольшее число ", max(list))
