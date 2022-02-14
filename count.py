# dict1={'w':0,'3':0,'r':0,'e':0,'s':0,'o':0,'u':0,'r':0,'c':0,'e':0}
# string='w3resource'
# for i in string:
#     if i=='w':
#         dict1['w']=dict1["w"]+1
#     elif i=='3':
#         dict1['3']=dict1['3']+1
#     elif i=='r':
#         dict1['r']=dict1['r']+1
#     elif i=='e':
#         dict1['e']=dict1['e']+1
#     elif i=='s':
#         dict1['s']=dict1['s']+1
#     elif i=='o':
#         dict1['o']=dict1['o']+1
#     elif i=='u':
#         dict1['u']=dict1['u']+1
#     elif i=='r':
#         dict1['r']=dict1['r']+1
#     elif i=='c':
#         dict1['c']=dict1['c']+1
# print(dict1)

dic={}
string = input("enter the string: ")
i=0
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[j]==string[i]:
            count=count+1
            dic.update({string[i]:count})
        j=j+1
    i=i+1
print(dic)
