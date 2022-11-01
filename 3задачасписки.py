list = (input("Введите некоторое количество слов через пробел:\n")).split()
if list == []:
    print("Ошибка")
else:
    print(set(list))