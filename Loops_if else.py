# age = int(input())

# if age >= 18:
#     print("You are Eligible")
# else:
#     print("Not Eligible",{18-age})

# ----------------

# maths = int(input())
# sci = int(input())
# eng = int(input())

# total = maths + sci + eng
# avg = total/3

# if maths > 40 and sci > 40 and eng > 40:
#     if avg > 80 and avg <= 100:
#         print("A grade")
#     elif avg <=80 and avg > 60:
#         print("B Grade")
#     elif avg <=60 and avg > 40:
#         print("C Grade")
# else:
#     print("Fail")
    

#  -------------------------------------------------

# Loops  
# 1. while , 2. for loop

# // Intialization (Start Point)
# while(condition)
# {
#     // statements
#     // Flow
# }

# w = 25   # Intialization

# while w <= 100:   # Condition
#     print(w,end='   ')      # statements
#     w += 1   # w = w + 1  FLow


w = 100   # Intialization

while w >= 25:   # Condition
    if w % 5 == 0 and (w % 7 == 0 and w % 10 == 0):
        print(w,end='   ')      # statements
    w -= 1   # w = w + 1  FLow



# Opearator

# Membership O/p  -> in,  not in

# list1 = [1,290, 89, 89, 78, 67]


# for(i=1;i<=90;++i)
# {

# }

# for i in range(10):   # default 0 end  = 10 (n-1)
#     print(i)
# for i in range(2,13):   # default 2 end  = 13 (n-1)
#     print(i)
# for i in range(2,13,1):   # default 2 end  = 13 (n-1) , step - default 1 (n-1)
#     print(i) 
# for i in range(2,13,2):   # default 2 end  = 13 (n-1)
#     print(i)
# for i in range(5,124,4):   # default 2 end  = 13 (n-1)
#     print(i)    # 5 9 .....
# for i in range(10,3):  
#     print(i)    # No answer


# for i in range(10,3,-1):  
#     print(i)    # 10 to 4
for i in range(40,3,-4):  
    print(i)    # No answer


for h in range(16):
    if h==5:
        continue
    print(h)

for h in range(16):
    if h==5:
        break
    print(h)
print("scvfdv")



for i in range(1,10):    # i = 1
    for j in range(3):   # j = 1
        print("Hello",j)   # H 0   H 1
        if i == j:       # True
            break
    print(j)           # 1

