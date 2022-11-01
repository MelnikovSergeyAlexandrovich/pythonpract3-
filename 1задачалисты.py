list = [(4,6,9), (5,5,5,5), (4,4,4)]
nummax = 0
j = 0
for i in list:
    setlist = set(i)
    for j in setlist:
            val = i.count(j)
            nummax = max(nummax,val)

print(f"Максимальное число повторений равно: {nummax}")