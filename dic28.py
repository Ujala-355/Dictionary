# n=[1,2,3,4]
# d={}
# for i in n:
#     d[i]={}
# print(d)
# # {1: {}, 2: {}, 3: {}, 4: {}}

# # 28 correct
n=[1,2,3,4]
new=c={}
for i in n:
    c[i]={}
    c=c[i]
print(new)
