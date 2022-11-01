stroka = str(input("Введите строку:\n"))
list = []
for i in stroka:
    list.append(i)

setlist = set(list)
print(f"Кол-во уникальных символов в данной строке равно {stroka}  = {str(len(setlist))}")
