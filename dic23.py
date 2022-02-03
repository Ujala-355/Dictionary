d={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
max=0
smax=0
tmax=0
mk=0
sk=0
tk=0
m=[]
for i in d:
    if d[i]>max:
        max=d[i]
        mk=i
for j in d:
    if d[j]>smax and d[j]<max:
        smax=d[j]
        sk=j
for k in d:
    if d[k]>tmax and d[k]<smax:
        tmax=d[k]
        tk=k
m.append(mk)
m.append(sk)
m.append(tk)
print(m)
