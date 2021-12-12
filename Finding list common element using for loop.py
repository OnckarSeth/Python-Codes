list_1 = [1, 5, 2, 9, 3, 4, 2, 5, 3, 9]
list_2 = []
for x in range(0, len(list_1)):
    if list_1[x] not in list_2:
        list_2.append(list_1[x])
    else:
        continue

print(list_2)
