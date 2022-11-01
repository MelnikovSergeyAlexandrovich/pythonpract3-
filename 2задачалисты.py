import datetime
dict = {}
number = int(input("Сколько людей нужно внести в словарь? \n"))
if number <= 0:
    print("Ошибка. Введите допустимое количество людей.")
    exit(0)

for i in range(number):
    sname = str(input("Введите фамилию: "))
    bday = (input("Введите дату рождения (Пример:27.12.2005) : "))
    email = str(input("Введите свою почту: "))
    dict[sname] = [bday, email]

data = input("Введите дату для проверки данных значений (Пример:27.12.2005) : ")
dataCheck = datetime.date(int(data.split(".")[2]),
                           int(data.split(".")[1]),
                            int(data.split(".")[0]))

for i in dict.keys():
    name = str(i)
    Exact = dict[i][0].split(".")
    day = int(Exact[0])
    month = int(Exact[1])
    year = int(Exact[2])
    dataExact = datetime.date(year,month,day)
    if dataExact > dataCheck:
        print (name)