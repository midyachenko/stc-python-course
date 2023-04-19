# todo: Вводится число, например: 1231.
# Вывести строчку, например: один два три один.
# Подсказка: создайте словарь

x = input('Enter number: ')
list_x = list(x)
num_dict = {"1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            "0": "zero"}
print(list_x)
result = []
for i in list_x:
    word = num_dict[i]
    result.append(word)
print(" ".join(result))

