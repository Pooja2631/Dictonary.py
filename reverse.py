# dict1={'Math':81, 'Physics':83, 'Chemistry':87}
# b={key:value for value,key in dict1.items()} 
# print(b)

dic={"A":[3,9,0,7],"B":[6,2,4,5]}
for x in dic:
    list1=[]
    a=len(dic[x])-1
    i=0
    while i<len(dic[x]):
        list1.append(dic[x][a])
        a=a-1
        i=i+1
    y=list1
    dic[x]=y
print(dic)