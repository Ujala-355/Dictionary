# a=[]
# for x in [1,2,3]:
#     for y in [3,4,5]:
#         if x!=y:
#             a.append((x,y))
# print(a)

# n=int(input("enter"))
# d=dict()
# for x in range(1,n+1):
#     d[x]=x**x
# print(d)

# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d={}
# for i in (d1,d2,d3):
#     d.update(i)
# print(d)

# d={"a":1,"b":2,"c":3,"d":4}
# i=input("enter")
# if i in d.keys():
#     print("keys",d[i])
# else:
#     print("not")

# d={"a":33,"b":45}
# print(d["a"])

# d={"apple":2,"banana":{"c":45,"d":33}}
# sum=0
# for i in d:
#     if type(d[i])==type({}):
#         for j in d[i]:
#             sum+=d[i][j]
#     else:
#         sum+=d[i]
# print(sum)

l1=["use","age","salary"]
l2=["danish"]