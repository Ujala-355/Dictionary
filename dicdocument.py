# 1
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
for i,j in d1.items():
    for x,y in d2.items():
        if i==j:
            d[i]=j+y
d.update(d1)
d.update(d2)
d.update(d[i])
print(d)

# # 3
# a=int(input("enter"))
# d=dict()
# for i in range(1,a+1):
#     d[i]=i*i
# print(d)

# # 4
# d=dict()
# for i in range(1,16):
#     d[i]=i**2
# print(d)

# # 7
# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d={}
# for i in (d1,d2,d3):
#     d.update(i)
# print(d)

# # 8
# d={"a":1,"b":2,"c":3,"u":10}
# k=input("enter a key")
# if k in d.keys():
#     print("key is present and value",d[k])
# else:
#     print("key isn't present")