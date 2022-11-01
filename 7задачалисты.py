def reverseLookup(di: dict, stroka: str):
    list = []
    for i in di.keys():
        if di[i] == stroka:
            list.append(i)
        return list

key1 = {"1" : "Sasha", "2": "Alex", "3" : " Serj"}
key2 = {"4": "Helen", "5 ": "Ishowspeed"}
print(reverseLookup(key1,'Sasha'))
print(reverseLookup(key2,'Alex'))






