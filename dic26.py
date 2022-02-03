# d={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,1]}
# x,y,z=d.values()
# for k in d:
#     print(k,end=" ")
# for i in x:
#     for j in y:
#         for l in z:
#             print(i,j,l)

# d={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,1]}
# for k in d:
#     print(k,end=" ")

# 26
d={"c1":[1,2,3],"c2":[5,6,7],"c3":[9,10,1]}
for j in d:
    print(j,end=" ")
print("")
# i=0
# while i<len(d):
#     for k in d:
#         print(d[k][i],end=" ")
#     print()
#     i+=1
for i in range(len(d)):
    for k in d:
        print(d[k][i],end="")
    print()





