# todo: На вход подается список, состоящий из списков чисел, например: [[1,5,3], [2,44,1,4], [3,3]].
#  Отсортируйте этот список по возрастанию общего количества цифр в каждом списке.
#  Каждый список отсортируйте по убыванию.

def el_sort(list):
    el_sort_list = []
    for i in (list):
        i.sort(reverse=True)
        el_sort_list.append(i)
    return el_sort_list

def custom_key(list):
    return len("".join(map(str, list)))


list1 = [[1, 5, 3], [2, 44, 1, 4], [3, 3]]
print("The unsorted list is:", list1)
el_sort_list = el_sort(list1)

el_sort_list.sort(key=custom_key)
print("The sorted list1 is:", el_sort_list)





