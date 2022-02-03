# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# for i in d.keys():
#     d[i]=[i for i in d[i] if i%2==0]
# print(d)

d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
for i in d.keys():
    d[i]=[i for i in d[i] if i%2==0]
print(d)