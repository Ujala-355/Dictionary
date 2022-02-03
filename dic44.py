d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
l=[]
x,y=d.values()
for i in range(len(x)):
    for j,k in d.items():
        y=({j:k[i]})
        l.append(y)
print(l)