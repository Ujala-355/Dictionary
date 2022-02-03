b="w3resource"
i=0
d={}
while i<len(b):
    j=0
    c=0
    while j<len(b):
        if b[i]==b[j]:
            c=c+1
        j+=1
    if b[i] not in d:
        d[b[i]]=c
    i+=1
print(d)
