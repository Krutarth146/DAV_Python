# Recursion

# when func. calls itself then it is called as Recursion

def fibonacci(num):
    i=0
    n1 = 0
    n2 = 1

    print(n1,n2)

    while i<num-2:
        n3 = n1 + n2
        print(n3,end=' ')

        n1 = n2
        n2 = n3
        i+=1

fibonacci(10)

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci_recursion(num):
    if num == 0:   # Base Condition
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)
    

# print(fibonacci_recursion(5))  # 0 1 1 2 3 5
print()
print()



import time

temp_1 = time.time()
for i in range(5):
    print(fibonacci_recursion(i))
print("Recursion: ",time.time() - temp_1)   # Recursion:  0.0010368824005126953





# iteration

def fibo_with_list(num):
    list3 = [0,1]

    for i in range(num):
        list3.append(list3[-1] + list3[-2])

    return list3[-2]

temp_2 = time.time()
print(fibo_with_list(5))  # 0 1 1 2 3 5 8
print("Iteration: ",time.time() - temp_2)  # Iteration:  0.002705097198486328

# map, reduce, filter, recursion ---> 5 Programs