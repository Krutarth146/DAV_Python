
# yield
def agnivesh(num):   # Defination
    for t in range(num):
        yield t
    
for i in agnivesh(5):
    print(i)   # 0

list1 = [i for i in agnivesh(5)]
print(list1)   # [0, 1, 2, 3, 4]

# lambda

def square(n1):
    return n1 * n1

print(square(24))   # 576

agni = lambda n2 : n2 * n2

print(agni(40))   # 1600

vishwa = lambda n3, n4 : n3 + n4

print(vishwa(10,90))

# ----------------

def doubler(num):
    return lambda x : x * num

kru = doubler(25)

print(kru(30))   # 750

# Quadratic Functions

def quadratic_fun(x):
    return lambda a,b,c : (a * x**2) + (b * x) + c

dev = quadratic_fun(5)

print(dev(10,20,30))   # 380

# H W 

list1 = ["Apple", 'Banana', 'Pery', 'Berry']

# list1.sort(reverse=True, key=lambda)   # Sort the list in basis of Second Element.   , lambda 10 Questions



# Map, Reduce, FIlter

list1 = [10,20,30,40,50]


kru1 = list(map(lambda x : x*x, list1))

print(kru1)   # [100, 400, 900, 1600, 2500]


base = [10,20,30,40]
power = [1,2,3,1]

kru2 = list(map(lambda x,y : x**y, base,power))
print(kru2)  # [10, 400, 27000, 40]

# -------------------------------
def royal(x,y):
    return x**y

kru2 = list(map(royal, base,power))
print(kru2)  # [10, 400, 27000, 40]



# if age == 18:
#     pass
# elif age <= 18:
#     sdcsc
# else:
#     pass

# sort que, lambda - 10, Map - 10 Que.
# Next Topic: reduce, filter, Numpy, Pandas, Matplotlib, csv, file, random