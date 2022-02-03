d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a=[]
for i in d:
    for j in i.values():
        a.append(j)
print(set(a))