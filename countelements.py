dict1={'M':0,'I':0,'S':0,'P':0}
A="MISSISSIPP"
for i in A:
    if i=='M':
        dict1['M']=dict1["M"]+1
    elif i=='I':
        dict1['I']=dict1['I']+1
    elif i=='S':
        dict1['S']=dict1['S']+1
    elif i=='P':
        dict1['P']=dict1['P']+1
print(dict1)