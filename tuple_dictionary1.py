list1 = [10,20,30,40,50]

tuple1 = (10, True, 'JK', "V", "Vishwa", {10,20,30},{"Name" : "Agnivesh", "Roll" : [10,20,30,40]},90.898, 90+9j, [23,3454], ((50,60),(30,40),(10,20)))
print(tuple1)  # (10, True, 'JK', 'V', 'Vishwa', {10, 20, 30}, {'Name': 'Agnivesh', 'Roll': [10, 20, 30, 40]}, 90.898, (90+9j), [23, 3454], ((50, 60), (30, 40), (10, 20)))
set1 = {}
print(type(set1))   # <class 'dict'>

set2 = {10,}
print(type(set2))   # <class 'set'>


tup1 = (10,20,101,10,10,10)  # Allow Duplicates, Ordered (Indexed), Immutable (Not Changeble)
print(tup1)   # (10, 20, 101, 10, 10, 10)

print(tup1[2])   # 101
print(tup1[-2])   # 10

print(tup1[2:5])  # (101, 10, 10)

print(tup1[-2:-5:-1])  # (10, 10, 101)
print(tup1[-4:-1:1])  # (101, 10, 10)

print(len(tup1))  # 6  -> starts from 1
print(sum(tup1))   # 161

print(tup1.count('10'))  # 0

# tup1 = [[]] * 3
# tup1[1] = 5
# print(tup1)  # [[], 5, []]

print(tup1.index(101))

for i in sorted(tup1[2:]):
    print(i)

tup1 = list(tup1)

tup1.insert(1,25)

tup1 = tuple(tup1)

print(tup1)   # [[], 5, []]




tup1 = tuple(set(tup1))
print(tup1)  # (25, 10, 20, 101)



unique = []

for i in tup1:
    if i not in unique:
        unique.append(i)
print(unique)

# ---------------------
tup1 = list(tup1)
for i in range(len(tup1)):
    temp = tup1[i]
    if tup1.count(temp) > 1:
        tup1.remove(temp)
 
print(tup1)   # [25, 10, 20, 101]


# # Write a program to check if the letter ‘j’ is present in the word 'Python'.

'''
Tasks in tuple -: 

1. Python program to find the size of a tuple
-> tuple = ("python", "includehelp", 43, 54.23)

2. Python program for adding a Tuple to List and Vice-Versa
-> tuple = ("python", "includehelp", 43, 54.23)

3. Python program to find the maximum and minimum K elements in a tuple
-> 
Input: 
myTuple = (4, 2, 5,7, 1, 8, 9), k = 2

Output: 
(9, 8) , (1, 2)

4. Python program to create a list of tuples from given list having number and its cube in each tuple
->
Input: 
list = [4, 1, 6, 2]

Output: 
[(4, 64), (1, 1), (6, 216), (2, 8)]

5. Python program to remove all tuples of length K
-> 
Input:
[(1, 4), (2), (4,5,6,8), (26), (3, 0, 1), (4)] k = 1

Output:
[(1, 4), (4, 5, 6, 8), (3, 0, 1)]

6. Python program to extract digits from tuple list
->
Input: 
list = [(4, 62), (2, 65), (5, 9), (0,1)]

Output:
[4, 6, 2, 5, 9, 0, 1]

7. Python program to find all pairs combination of two tuples
->
Input:
tup1 = (1, 2), tup2 = (5, 7)

Output:
[(1, 5), (1, 7), (2, 5), (2, 7), (5, 1), (5, 2), (7, 1), (7, 2)]

8. Python program to join tuples if similar initial element
->
Input:
list = [(1, 4), (3, 1), (1, 2), (4, 2), (3, 5)]

Output:
list = [(1, 4, 2), (3, 1, 5), (4, 2)]

9. Python program to sort a list of tuples by second item
->
Input:
[(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]

Output:
[(9, 1), (2, 5), (4, 6), (1, 7), (2, 8)]

10. Python program to sort a list of tuples in increasing order by the last element in each tuple
-> tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]

11. Python program to sort tuples by frequency of their absolute difference
-> 
Input:
[(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

Output:
[(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]

12. Python program to remove duplicate tuples irrespective of order
->
Input:
tupList = [(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

Output:
[(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

13. Python program to order tuples by list
->
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]

14. Python program to concatenate maximum tuples
->
Input:
tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3)]

Output:
"python programming"

15. Python program to flatten tuple of lists to a tuple
->
Input:
([4, 9, 1], [5 ,6])

Output:
(4, 9, 1, 5, 6)
'''




# ----------------------------------------------------------------------------------------

# Dictionary

dict1 = {"Name" : "Krutarth Patel", 'Roll' : 90, "marks" : 90, 'percentage' : [10,20,30,40], "Name" : "Herry"}
print(dict1)   # {'Name': 'Herry', 'Roll': 90, 'marks': 90.89, 'percentage': [10, 20, 30, 40]}


# Name, ROll , marks, percentage are Keys() -> Unique, (Primary)

# "Krutarth Patel", 90, 90.89 are values -> Allow's Duplicates

# print(dict1[0])

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable (Mutable). No duplicate members.

print(dict1['Roll'])   # 90

dict1['Name'] = "Ayush"
print(dict1)


dict1.update({"Gender" : "Male"})
print(dict1)  # {'Name': 'Ayush', 'Roll': 90, 'marks': 90, 'percentage': [10, 20, 30, 40], 'Gender': 'Male'}

print(dict1.keys())   # dict_keys(['Name', 'Roll', 'marks', 'percentage', 'Gender'])
print(dict1.values())   # dict_values(['Ayush', 90, 90, [10, 20, 30, 40], 'Male'])
print(dict1.items())   # dict_items([('Name', 'Ayush'), ('Roll', 90), ('marks', 90), ('percentage', [10, 20, 30, 40]), ('Gender', 'Male')])


for i in dict1:
    print(i)

for j in dict1.keys():
    print(j)


for k in dict1.values():
    print(k)

for y in dict1.items():
    print(y,end=' ')  # ('Name', 'Ayush') ('Roll', 90) ('marks', 90) ('percentage', [10, 20, 30, 40]) ('Gender', 'Male')
print()
for vishwa,herry in dict1.items():
    print(vishwa,herry)

x = ('liat1','list2','list3')
y = 20
thisdict = dict.fromkeys(x,y)
print(thisdict)  # {'liat1': 20, 'list2': 20, 'list3': 20}


print(dict1['Gender'])   # Male
print(dict1.get('Gender'))   # Male


print(dict1)   # {'Name': 'Ayush', 'Roll': 90, 'marks': 90, 'percentage': [10, 20, 30, 40], 'Gender': 'Male'}
# dict1.pop('Gender')
# print(dict1)   # {'Name': 'Ayush', 'Roll': 90, 'marks': 90, 'percentage': [10, 20, 30, 40]}

# # del dict1
# dict1.clear()
# print(dict1)   # {}
# x = dict1.popitem()
# print(dict1)  # dict.popitem() takes no arguments
# print(x)

# v = dict1.pop('Gender')
# print(v)   # Male

# print(dict1)  # {'Name': 'Ayush', 'Roll': 90, 'marks': 90, 'percentage': [10, 20, 30, 40]}

# dict1.update({"Organization" : "ROyal", "list1" : "sdvsdv"})
# print(dict1)   # {'Name': 'Ayush', 'Roll': 90, 'marks': 90, 'percentage': [10, 20, 30, 40], 'Gender': 'Male', 'Organization': 'ROyal'}


dict1 = ({"name" : "Manoj","name1" : "Manoj"}, {"Roll" : 908}, {"Address" : "Ahm"})
print(dict1)


for i in dict1:
    # print(type(i))
    print(i.items())


str1 =  "Mississippi"

# Ans - {'M' : 1, 'i' : 4, 's' : 4, 'p' : 2}

list1 = list(str1)
print(list1)  # ['M', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

dict6 = {}
for i in list1:
    if i not in dict6:
        dict6[i] = 1
    else:
        dict6[i] += 1
print(dict6)



# Tasks
'''
1. Check if a Given Key Already Exists in Dictionary
-> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

D1 = {'first_name' : 'Krutarth', 'age' : 22, 'height' : 5.0 , 'job' : 'Developer', 'company': 'Google'}

2. Handle Missing Keys in Dictionary
-> Dictionary is a collection in python, where the data is stored in the form of a key-value pair, that is, it maps key to its value. Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

3. Extract Unique Values in a Given Dictionary
-> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }

Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]

4. Print the Sum of Key Value Pairs in a Given Dictionary
-> You need to create a list which has the sum of key-value pairs of a given dictionary. 

D1 = {2: 8, 5: 20, 3: 15}



HINT-> This can be done using a for loop and append() function. 

5. Replace Dictionary Values From Other Dictionary
-> Let’s say you are given two dictionaries. You need to write a python program that will replace the values in the first dictionary with the values from the second dictionary if the key is present in the second dictionary. 

# initializing D1 - first dictionary
D1 = {'first_name' : 'Rutvi', 'age' : 21, 'height' : 4.0 , 'job' : 'Software Engineer', 'company': 'Uber'}
 
# initializing D2 - - first dictionary
D2 = {'age' : 35, 'job' : 'senior data analyst'}

6. Update or Change the Keys in a Given Dictionary
-> try these 2 ways
i)  Using assignment operator
ii) Using pop() method

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

7. Delete a List of Keys in a Given Dictionary 

8. Count the Frequency of List Items Using a Dictionary
-> You can solve this in many ways. Any ideas? Well, you can just use looping constructs or use the list() count method or you can start with an empty dictionary and use the dict.get() method. Probably many other ways!

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

9. Change the Value of a Key in Nested Dictionary
-> Given a nested dictionary, you need to write a program demonstrating how to change the value associated with a particular key of that dictionary. 

#change the value of a key in nested dictionary
#Initializing Dictionary
D1 = {'emp1': {'name' : 'Niraj', 'age' : 21, 'job' : 'developer'}, 
      'emp2': {'name' : 'Zafar', 'age' : 22, 'job' : 'data analyst'}, 
      'emp3': {'name' : 'Rutvi', 'age' : 22, 'job' : 'data scientist'}, 
      'emp4': {'name' : 'Krutarth', 'age' : 60, 'job' : 'python developer'}}

11. Check if the Given Dictionary Is Empty or Not
-> One way to check this using the len() function, which you can try coding; we will achieve this using the bool() function. The bool() function evaluates to standard true or false and is used to return or convert a value to Boolean type. If you pass an empty dictionary, the bool() evaluates to False, as failure to convert something that is empty.

14. Get a Key From Value in a Dictionary
-> You need to write a program, which returns the key for a given value. This can be done in multiple ways. Try doing it using dict.items() function.

#get key for a given value using dict.items()
# Dictionary Initialization
D1 = {'Priyanka Chopra': 23, 'Alia Bhatt': 29, 'Hritik Roshan': 45, 'Ranbir Kapoor': 40}

15. Sort a Given Dictionary by Key
-> You know this so, you got this...

D1 = {'Niraj': 23, 'Jaynam': 29, 'Rutvi': 40, 'Zafar': 45, 'Obama': 34}
'''


D1 = {2: 8, 5: 20, 3: 15}

for i,j in D1.items():
    print(i+j)


D1 = {'emp1': {'name' : 'Niraj', 'age' : 21, 'job' : 'developer'}, 
      'emp2': {'name' : 'Zafar', 'age' : 22, 'job' : 'data analyst'}, 
      'emp3': {'name' : 'Rutvi', 'age' : 22, 'job' : 'data scientist'}, 
      'emp4': {'name' : 'Krutarth', 'age' : 60, 'job' : 'python developer'}}

D1['emp1']['age'] = 900
print(D1)