list = []

while True:
    number = int(input("Введите целое число: \t"))
    list.append(number)
    if number == 0:
        break
list.remove(0)
print(sorted(list, reverse = True))