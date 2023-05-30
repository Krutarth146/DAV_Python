# Map, reduce, filter

list1 = [20,77,44,22,11,88]

def square_area(list1):
    area = []
    for i in list1:
        area.append(i*i)
    return area

print(square_area(list1))  # [400, 5929, 1936, 484, 121, 7744]

print(list(map(lambda x : x*x, list1)))  # [400, 5929, 1936, 484, 121, 7744]

str1 = ['10', '30','40','90']
print(list(map(int, str1)))  # [10, 30, 40, 90]


temp = [("Ahm", 45), ("Kheda", 33), ('Vadodara',44)]  # celicius ---> fahernheit


print(list(map(lambda temp: (temp[0],((9//5) * temp[1]) + 32), temp)))  # [('Ahm', 77), ('Kheda', 65), ('Vadodara', 76)]


# filter

list1 = [20,77,44,22,11,88]

sum = 0
for i in list1:
    sum += i
print(sum)   # 262
print(sum/len(list1))   # 43


import statistics

print(statistics.mean(list1))


tup1 = tuple(filter(lambda x : x > statistics.mean(list1), list1))
print(tup1)  # (77, 44, 88)


# reduce 
list1 = [20,77,44,22,11,88]
from functools import reduce

print(reduce(lambda x,y : x+y, list1))  # 262

import operator
print(reduce(operator.add, list1))  # 262

from itertools import accumulate

print(list(accumulate( list1,lambda x,y : x+y)))  # [20, 97, 141, 163, 174, 262]

