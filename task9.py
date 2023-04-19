# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

x = input("X= ")
if x.isdigit():
    x = int(x)
    c = x // 100
    y = x % 100
    if y == 0:
        print("It is ", c, " century")
    else:
        print("It is ", c + 1, " century")
else:
    print("It is not digits")
