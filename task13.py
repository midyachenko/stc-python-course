'''todo:  Ввести число n. Напечатать треугольник из символов +.
Пример для n = 5:
+
++
+++
++++
+++++'''

def triangle(n):
    for i in range (1, n):
        print("+"*i)

n = int(input("N= "))
triangle(n)
