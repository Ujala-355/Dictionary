d={"a":10,"b":5,"c":{"f":2,"g":{"h":23,"u":{"x":12,"y":8}}}}
for i in d:
    if type(d[i])==type({}):
        for j in d[i]:
            if type(d[i][j])==type({}):
                for k in d[i][j]:
                    if type(d[i][j][k])==type({}):
                        for l in d[i][j][k]:
                            if d[i][j][k][l]%2==0:
                                print(d[i][j][k][l],"even")
                            else:
                                print(d[i][j][k][l],"odd")
                    else:
                        if d[i][j][k]%2==0:
                            print(d[i][j][k],"even")
                        else:
                            print(d[i][j][k],"odd")
            else:
                if d[i][j]%2==0:
                    print(d[i][j],"even")
                else:
                    print(d[i][j],"odd")
    else:
        if d[i]%2==0:
            print(d[i],"even")
        else:
            print(d[i],"odd")