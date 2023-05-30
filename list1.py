# array = [10,20,30,40,50,90] -> int

list1 = [10, 89.90, 'Jeet', 'A', True, False, 90+8j, [10,90,89], (20,30,40), {90,90,90}, {"Name" : "Raghav"}]

print(list1)  # [10, 89.9, 'Jeet', 'A', True, False, (90+8j), [10, 90, 89], (20, 30, 40), {90}, {'Name': 'Raghav'}]

print(list1.__sizeof__())   # 128

print(id(list1))  # 2470441398976

print(len(list1))  # 11 -> Length starts from 1

list1 = [10,90,89,78,67]
list2 = [10,90,89,78,67]

# print(id(list1))  # 2509618036288
# print(id(list2))  # 2509618033344

# x = 90
# y = 90

# print(id(x))  # 2607050787856
# print(id(y))  # 2607050787856


list1 = [10,20,30,40,50]


list2 = list1.copy()   # Shallow Copy
list3 = list1          # Deep Copy

print(id(list1))  # 2048495725120
print(id(list2))  # 2048495664704  # id - Different
print(id(list3))  # 2048495725120


list1 = [10, 90, 78, 67, 57, 57, 57 ]  # Allow Duplicates, Ordered (Indexed), Mutable (Changeble)

# Indexing
print(list1[0])   # 10
print(list1[6])   # 57
print(list1[-4])   # 67
print(list1[-7])   # 10

# Slicing
# print(list1[start : End(n-1) : step(n-1)])   # 10

print(list1[2:5])  #  [78, 67, 57]
print(list1[6:1])  #  []
print(list1[:])  #  [10, 90, 78, 67, 57, 57, 57]
print(list1[:4])  #  [10, 90, 78, 67]
print(list1[1:6:1])  #  [90, 78, 67, 57, 57]
print(list1[1:6:3])  #  [90, 57]
print(list1[::2])  #  [10, 78, 57, 57]


print(list1[10:3:2])  # []
print(list1[5:1:-2])  # [57, 67]

list1 = [10, 90, 78, 67, 58, 57, 59 ] 
print(list1[-2:-6:-2])  # [57, 67]

print(list1[-3:2:2])   # []


list1 = [[10,20,30], 
         [40,50,60], 
         [70,80,90]]
print(len(list1))


for _agni in list1:
    print(_agni,end=' ')  # [10, 20, 30]  [40, 50, 60]  [70, 80, 90]

for _ in list1:  # [10, 20, 30]
    for jeet in _:  # 10
        print(jeet,end=' ')  # 10 20 30 40 50 60 70 80 90


print()

def Transpose(list10):
    list2 = []
    for row in range(len(list10)): # 0 1 2
        for col in range(len(list10)):  # 0 1 2
            list2.append(list10[col][row])  # list1[0][0]
    return list2

print(Transpose(list1))


# for i in range(1,3):
#     print(i)

# print(i)

# i = 90
# while i>=80:
#     if i % 5 ==0:
#         print(i)
#         print("Ram")
#         print("Sita")
#     if i == 85:
#         break
#     i-=1


# List Methods

list1 = [10,290,90,89,45,78]

print(len(list1))  # 6  -> starts from 1, Index starts from 0

# list1.append(100)
# print(list1)  # [10, 290, 90, 89, 45, 78, 100]

# list1.append("Agni")
# print(list1)  # [10, 290, 90, 89, 45, 78, 100, 'Agni']

# # list1.extend(100)
# # print(list1)  # int' object is not iterable (Error)

# list1.extend("300")
# print(list1)  # [10, 290, 90, 89, 45, 78, 100, 'Agni', '3', '0', '0']
list1  = [10,290,90,89,45,78]
list2  = [10,20,30,40]

list1.append(list2)
print(list1)  # [10, 290, 90, 89, 45, 78, [10, 20, 30, 40]]

# list1.extend(list2)
# print(list1)  # [10, 290, 90, 89, 45, 78, 10, 20, 30, 40]

list1.insert(2,900)
print(list1)  # [10, 290, 900, 90, 89, 45, 78, [10, 20, 30, 40]]

list1.insert(-1,500)
print(list1)  # [10, 290, 900, 90, 89, 45, 78, 500, [10, 20, 30, 40]]

list1.pop()
list1.pop()
print(list1)  # [10, 290, 900, 90, 89, 45, 78]

list1.pop(3)
print(list1)  # [10, 290, 900, 89, 45, 78]

list1.remove(290)
print(list1)  # [10, 900, 89, 45, 78]

# list1.clear()
# print(list1)   # []

list2 = list1.copy()   # Shallow Copy
print(list2)

list3 = list1  # Deep Copy

list1.append(4000)

print("List2: ",list2)  # List2:  [10, 900, 89, 45, 78]
print("List3: ",list3)  # List3:  [10, 900, 89, 45, 78, 4000]

list3.append(8000)
list3.append(8000)
print("list1: ",list1)  # list1:  [10, 900, 89, 45, 78, 4000, 8000, 8000]


print(list1.count(8000))  # 2
print(list1.index(8000))  # 6

for i in range(len(list1)):   # 0 to 7
    if list1[i] == 8000:  # list1[0]
        print(i)

list1.reverse()
print(list1)  # [8000, 8000, 4000, 78, 45, 89, 900, 10]

list1.sort()
print(list1)   # [10, 45, 78, 89, 900, 4000, 8000, 8000]

list1.sort(reverse=True)
print(list1)   # [8000, 8000, 4000, 900, 89, 78, 45, 10]  # In decresing Order


'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''

# from nsetools import Nse
# nse = Nse()
# print(nse)


# # quote = nse.get_quote('RELIANCE')
# # print(quote)

# from pprint import pprint

# # pprint(q)

# all_stock_codes = nse.get_stock_codes()
# print(all_stock_codes)


from nsepy import get_history
from datetime import datetime

# You can change the dates accordingly
start = datetime(2019, 7, 15)
end = datetime(2019, 7, 30)

data = get_history(symbol='NIFTY',start=start,end=end, index=True)