# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

x = input("X= ")
if x.isdigit() and len(x) == 4:
    if x[0]== x[3] and x[1] == x[2]:
        print("True")
    else:
        print("False")
else:
    print("It is bad number")