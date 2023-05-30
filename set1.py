set1 = {}

print(type(set1))  # <class 'dict'>

set1 = {10}
print(type(set1))  # <class 'set'>

set2 = {10,90.89,"Aman", ("aman", 'Agni'), True, 90+8j,10,10}

print(set2)  # {True, ('aman', 'Agni'), (90+8j), 90.89, 'Aman', 10}

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

print(id(set1))  # 2296294842528
print(set1.__sizeof__())  # 200

# print(set1[0]) # Gives Error

for i in set2:
    print(i)

set2.add("Amana")
print(set2)  # {('aman', 'Agni'), True, (90+8j), 90.89, 'Amana', 10, 'Aman'}

# set2.clear()
# print(set2)  # set()

# del set2

set1 = set2.copy()   # Xerox
 
set3 = set2   # Digilocker

set2 = {10,20,30,40,50}
set3 = {1,2,3,40,50}
# print(set2.difference(set3))   # {10, 20, 30}


# # set2.difference_update(set3)
# # print(set2)  # {20, 10, 30}

# set2.discard(10)
# print(set2)  # {50, 20, 40, 30}

# print(set2.intersection(set3))  # {40, 50}


# set2.intersection_update(set3)
# print(set2)

set2 = {10,20,30,40,50}
set3 = {1,2,5}

print(set2.isdisjoint(set3))  # True
print(set2.issuperset(set3))  # False
print(set3.issubset(set2))   # False


print(set2.pop())  # 50
print(set2)  # {20, 40, 10, 30}


set2.remove(30)  # Generates Error if element is not Found
print(set2)   # {20, 40, 10}

set2.discard(22)  # Work Properly even element is not Found
print(set2)

set2 = {10,20,30,40,50}
set3 = {1,2,40,50}
print(set2.symmetric_difference(set3))  # {1, 2, 10, 20, 30}

print(set2.union(set3))  # {1, 2, 40, 10, 50, 20, 30}


list1= [33,90,11,23,67]
set2.update("Manish")
set2.update(list1)
print(set2)  # {67, 10, 11, 's', 20, 23, 'M', 90, 'n', 30, 33, 'i', 'h', 40, 'a', 50}


# print(enumerate(set2))


for i in enumerate(set2):
    print(i)
for i in sorted(set3):
    print(i)

set4 = {"", 90, 56}
print(all(set4))  # False
# Frozen set


'''

# Set Tasks


 Find the Differences Between Two Lists Using Sets
Check if a Given String Is Heterogram or Not
 Find Maximum and Minimum Values of a Set
Get All the Subsets of a Given Size in a Set
 Determine if Two Sets Are Disjoint or Not Without In-built Methods
Remove the Given Items of a Set at Once
 Count Number of Vowels in a Given String Using Sets
Convert a Set to String
 Find Common Elements of Three Given Lists Using Sets
Square the Elements of Set Using for Loop
 Check if a Set Is Superset Itself or Another Given Set
Perform Intersection of Two Lists Using Set Methods
 Check if a Given Value Is Present in the Set or Not
'''