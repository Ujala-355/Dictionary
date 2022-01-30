d={"a":100,"b":45,"c":30,"d":22,"e":55,"f":57,"s":95}
i=0
b=[]
for j in d:
    b.append(d[j])    
max=0
min=b[i]
for i in range((len(b))):
    if b[i]>max:
        max=b[i]
    if b[i]<min:
        min=b[i]
print(max)
print(min)

