def vishwa(num1 , num2, num3=0):
    print("This is Vishwa Function")
    print(num1 + num2 + num3)

vishwa(10,30,34)  # 40  # Default Function


print(vishwa(30,210))   # None


def Agni(a, b, *kru, k=90):
    for i in kru:
        print(i,end=' ')  # 30 Agnui2 89.9
    print(k)   # 90

Agni(10,20,30,"Agnui2", 89.90)   # (10, 20, 30, 'Agnui2', 89.9)


# kwargs  -->  Dictionary

# key,value Pairs


def patel(**royal):
    # print(royal)
    for k,f in royal.items():
        print(k,f)

patel(name="Manoj", roll = 50, school = "HBK")  # {'name': 'Manoj', 'roll': 50, 'school': 'HBK'}

# Powerful function

# yield, enumerate, zip, map, reduce, filter, lambda

# Modules -> numpy, matplotlib, pandas, random, datetime


# def Shr(num):
#     for i in range(num):
#         return i
    

# print(Shr(5))


def Shr_sol(num):
    for i in range(num):
        yield i

for g in Shr_sol(5):
    print(g,end=' ')  # 0 1 2 3 4


list1 = [10,20,30,40,50]
list2 = [2,5,8,10,12,9000]

print()
ans = [_ for _ in zip(list1,list2)]
print(ans)   # [(10, 2), (20, 5), (30, 8), (40, 10), (50, 12)]

list2 = [2,5,8,10,12,9000]

res = [w for w,k in enumerate(list2,100)]
print(res)  # [(100, 2), (101, 5), (102, 8), (103, 10), (104, 12), (105, 9000)]


# lambda  --> refer (5 Que.)

ans = lambda x: x % 2 == 0

print(ans(20))   # 400

list1 = ["Manoj"]
list1[0] = 90

print(list1)