# todo: На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении.

x = input('Enter text: ')
lst = x.split()
print(lst)
max = 0
max_word = ''
for i in lst:
    l = len(i)
    if l > max:
        max = l
        max_word=i
    else:
        continue
print("Cамое длинное слово в этом предложении - ", max_word)
