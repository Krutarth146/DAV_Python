list1 = [[10,90,67], 
         [56,89,32], 
         [78,32,11]]

copy1 = list1.copy()

d1 = []
for i in list1:
    for j in i:
        d1.append(j)

d1.sort()
print(d1)


k=0
for i in range(len(list1)):  # 3
    for j in range(len(list1[i])):
        copy1[i][j] = d1[k]
        k+=1


print(copy1)