d1={"a":100,"b":200,"d":300}
d2={"a":300,"b":200,"c":400}
d={}
for i in d1:
    for j in d2:
        if i==j:
            k=d1[i]+d2[j]
            d.update({i:k})
d.update({"c":400})
d.update({"d":300})
print(d)

