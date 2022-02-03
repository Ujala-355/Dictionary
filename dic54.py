d={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
l=[]
for k,v in d.items():
    for i in v:
        d={k:i}
        l.append(d)
print(l)