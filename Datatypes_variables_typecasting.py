# Python is Dynamic Language

# float x = 90;

# Variables

# Datatypes -> Numbers -> Int, float, Complex

x = 9000000000000000000000000000000000000000000000
print(x)   # 9000000000000000000000000000000000000000000000
print(type(x))  # <class 'int'>

_dhiraj_sir = 8121231312321321313130.78
print(type(_dhiraj_sir))  # <class 'float'>

rishi = 4 + 90j
print(type(rishi))  # <class 'complex'> -> 4 is Real part, 90j is Imaginary Part

f = 5
print(rishi + f)  # (9+90j)

j = True

print(type(j))  # <class 'bool'>

j = False
print(type(j)) # <class 'bool'>

h = 'A'
print(type(h))  # <class 'str'>

'''
dfvdfvd
dvdfvd
vdf
'''

Herry = "Dev Bhatt"
print(Herry)  # Dev Bhatt
print(type(Herry))  # <class 'str'>


# TypeCasting
# -> To convert from one Datatype into another Datatype
# 1. Implicit Typecasting    2. Explicit Typecasting

s = 90
g = 80.78

print(s+g)  # 170.78   # Implicit Typecasting

t = '40'
p = 80
# print(t+p)
print(int(t)+p)  # 120  # Explicit Typecasting

f = "30"
j = "10"
print(f,j,sep='\n')
print(f+j)   # 3010
print(int(f)+int(j))   # 40


g = 70  # int
w = True  # bool -> 1  

print(g+w)  # 71


t = '89.80'
print(int(float(t)))   # 89


import math

print(math.ceil(89.01))  # 90
print(math.floor(89.99))  # 89

# printf("Enter any Num: ");
# scanf("%d",&num1)

# num1 = input("Enter Number: ")
# num2 = input("Enter Number: ")
# print(num1 + num2)   # 50100
num1 = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
print(num1 + num2)   # 60
print(num1, '+', num2 , "=", num1+ num2)  # 2 + 90 = 92
print(f'{num1} + {num2} = {num1+num2}')   # 2 + 90 = 92  # fstring  # Adv. formatted str


# Calc