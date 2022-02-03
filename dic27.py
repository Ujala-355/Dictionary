s=[{"id":1,"succes":True,"name":"Lary"},{"id":2,"succes":False,"name":"Rabi"},{"id":3,"succes":True,"name":"Alex"}]
# c=0
# sum=0
# for i in s:
#     if i["id"]: 
#         c+=1  
# print(c)

# 27
sum=0
a=input("enter")
for i in s:
    for j in i:       
       if j==a:
            sum+=i[j]
print(sum)           