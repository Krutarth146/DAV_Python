l1 = [10,20,30,40,55,33]

num1 = 21

def cube(dev):
    return dev ** 3

print(cube(num1))  # 9261

x = lambda dev : dev ** 3
print(x(num1))   # 9261

l1 = [10,20,30,40,55,33]
res = []
for i in l1:
    res.append(i**3)
print(res)  # [1000, 8000, 27000, 64000, 166375, 35937]

# Powerful Functions map, reduce, filter
l1 = [10,20,30,40,55,33]
x = list(map(lambda x : x+2000, l1))
# print(x)  # <map object at 0x00000196BFEBAE60>
print(x)  # [2010, 2020, 2030, 2040, 2055, 2033]

char_list = ['A', 'B']

print(tuple(map(lambda x : chr(ord(x) + 32),char_list)))

# --------------------------

# Nested Lambda

vishwa = lambda x = 10: lambda \
c,v : \
    x**c + v

print(vishwa()(3,4))  # 1004


# print(agni(2,6))  # 106


# Generators
x = 90   # Global Variable

def loop1(num = 80):
    global x
    x+=10
    print(x,num)   # 100
    # for i in list(reversed(range(5))):
    #     yield i
loop1(5000)  # 100
print(x)  # 100
# def loop2():
#     yield "dev"
#     yield "Agni"
#     yield "Vishwa"

# for i in loop2():
#     print(i)

# x = loop1(5).__next__()
# print(x)

# print(loop2().__next__())
# print(loop2().__next__())


# FUnctions--> 4 Types, Default Func, Args, Kwargs, Local-global, Recursion,lambda, Nested Lambda, Map, reduce, filter, Iterators, Generators


# Dictionary Tasks