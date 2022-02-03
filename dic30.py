d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

# a="ujala n"
# i=0
# while i<len(a):
#     j=0
#     str=""
#     while j<len(a):
#         if a[j] not in " ":
#             str+=a[j]
#         j+=1
#     i+=1
#     print(str)
#     break
  
  
# 30 currect
for i in d:
    str=""
    for j in i:
        if j!= " ":
            str+=j
    print(str)    


