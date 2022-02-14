# dict1={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# dic={}
# for i in dict1:
#     dic[i]=[]
# print(dic)


dict1={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
for i in dict1:
    dict1[i].clear()
print(dict1)