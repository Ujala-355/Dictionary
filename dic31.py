# 31
d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
smax=0
tmax=0
for i in d:
    if d[i]>max:
        max=d[i]
for j in d:
    if d[j]>smax and d[j]<max:
        smax=d[j]
for k in d:
    if d[k]>tmax and d[k]<smax:
        tmax=d[k]
print(max)
print(smax)
print(tmax)
