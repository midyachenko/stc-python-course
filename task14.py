#todo: Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.

lst = [int(i) for i in input().split()]
print(lst)
lst.sort()
print('Min = ', lst[0])