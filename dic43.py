d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
k={}
for i in d:
    if i[0] not in k.keys():
        k.update({i[0]:[i[1]]})
    elif i[0] in k.keys():
        k[i[0]].append(i[1])
print(k)

