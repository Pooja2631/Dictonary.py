a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in (a):
#     a2=(i.values())
#     if a2 not in b:
#         b.extend(a2)
# print(b)


lis=[]
dic={}
for x in a:
    for i in x:
        if x[i] not in lis:
            lis.append(x[i])

print(lis)