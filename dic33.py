# s = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# name=input("enter a name")
# for i in s:
#         if s[i]==name:
#             name=s[i]
# print(s[i])

# 33 currect
s={'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for i in s:
    print(i)
    for j in s[i]:
        print(j,s[i][j])

