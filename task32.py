#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
#Ввод: GGCTAA
#Вывод: CCGATT

dnk = "GGCTAA"
def dnk_rnk(dnk):
    rnk = ""
    for i in list(dnk):
        match i:
            case 'G':
                j = 'C'
            case 'C':
                j = 'G'
            case 'T':
                j = 'A'
            case 'A':
                j = 'T'
        rnk += j
    return rnk

print(dnk_rnk(dnk))