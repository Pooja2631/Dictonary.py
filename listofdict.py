list1=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
i=1
a=[]
while i<len(list1):
    for j in list1[i]:
        if list1[i][j] not in a:
            a.append(list1[i][j])
    i=i+1
print(a)

# list1=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# i=1
# a=[]
# while i<len(list1):
#     for j in list1[i]:
#         a.append(list1[i][j])
#     i=i+1
# print(a)
    
