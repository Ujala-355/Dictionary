d=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
dict={}
for i in d:
    b={i[0]:i[1:]}
    dict.update(b)
print(dict)