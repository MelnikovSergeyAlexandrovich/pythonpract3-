list = []

while True:
    number = input("Введите целое число: \t")
    if number == '':
         break
    list.append(int(number))

print(sorted(list), sep = "\n")

