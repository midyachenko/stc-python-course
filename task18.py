# todo: Дано множество, состоящее из чисел. Его можно ввести одной строкой с пробелами между числами
#  с помощью оператора tes=set(map(int, input().split())).
#  Напечатайте среднее арифметическое введенных чисел. Воспользуйтесь функциями sum и len.

tes = set(map(int, input("Enter numbers:").split()))
print(sum(tes)/len(tes))




