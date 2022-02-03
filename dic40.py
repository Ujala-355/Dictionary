d1=['S001', 'S002', 'S003', 'S004']
d2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
d3=[85, 98, 89, 92]
# d=dict(zip(d2,d3))
# print(d)
a=[{i:j} for i,j in zip(d2,d3)]
b=[{i:j} for i,j in zip(d1,a)]
print(b)





