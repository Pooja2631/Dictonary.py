dic={'1':['a','b'], '2':['c','d']}
for x in dic:
    i=0
    while i<len(dic[x]):
        j=1
        while j<len(dic[x]):
            print(dic[x][j])
            #print(dic[x][i]+dic[x][j])
            j=j+1
        i=i+1
    break