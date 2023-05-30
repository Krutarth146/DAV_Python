list1 = [10,20,30,40,50]

# print(list1)
# cube = []

# for x in list1:
#     cube.append(x*x*x)

# print(cube)


# cube = [(j*j*j*j) for j in list1]
# print(cube)  # [1000, 8000, 27000, 64000, 125000]

# square = [(j,j*j) for j in list1]
# print(square)  # [100, 400, 900, 1600, 2500]

# ans = [(10,1000), (20,8000), (30,27000)]

# list1 = [10, 20, 30]
# list2 = []
# for i in list1:
#     t = (i,i*100)
#     list2.append(t)
# print(list2)

# list1 = [1,2,3,4,5,6]

# list2 = [(i,i**3) for i in list1]
# print(list2)  # [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216)]

# list1 = [1,2,3,4,5,6]

# # for i in list1:
# #     for j in list1:
# #         print(i,j)

# ans = [(i,j) for i in list1 for j in list1]
# print(ans)  # [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for i in list1:
    if i % 2 != 0:
        list2.append(i)

print(list2)

odd = [i for i in list1 if i % 2 != 0]
print(odd)

# main = []

# freq= int(input("ENter frequency: "))

# for i in range(freq):
#     v = [int(i) for i in input().split()]
#     main.append(v)

# print(main)


que = [[10, 90, 89, 78], [23, 21, 34, 67], [77, 888, 88, 88], [55, 55, 55, 55]]

for i in que:   # [10, 90, 89, 78]
    for k in i:
        print(k)

ans = [k for i in que for k in i]
print(ans)  # [10, 90, 89, 78, 23, 21, 34, 67, 77, 888, 88, 88, 55, 55, 55, 55]

# Que: 

que_1 = [(10,2), (20,9), (50,8), (40,1)]   # sort by tuple's second Element
ans_1 = [(40,1), (10,2), (50,8), (20,9)]