d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
f=0
s=0
t=0
fu=0
fi=0
fk=0
sk=0
tk=0
fuk=0
fik=0
l1=[]
for i in d:
    if d[i]>f:
        f=d[i]
        fk=i
for j in d:
    if d[j]>s and d[j]<f:
        s=d[j]
        sk=j
for k in d:
    if d[k]>t and d[k]<s:
        t=d[k]
        tk=k
for l in d:
    if d[l]>fu and d[l]<t:
        fu=d[l]
        fuk=l
for m in d:
    if d[m]>fi and d[m]<fu:
        fi=d[m]
        fik=m
l1.append(fk)
l1.append(sk)
l1.append(tk)
l1.append(fuk)
l1.append(fik)
print(l1)




