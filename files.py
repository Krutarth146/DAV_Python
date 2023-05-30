# File

# fopen(), fclose()


# File Modes

# 't' - Text Mode

# 'b' - Binary Mode

# 'w' - write Mode  (If file not exists then it will create a new file) (Overwrite)

# 'r' - Read Mode (If file does not Exist then then it will generate an Error)

# 'a' - Append Mode (If file not exists then it will create a new file) (write data from last Position)

# '+' - read and write both Operations

fp = open("agni.txt",'w')
print(fp)  # <_io.TextIOWrapper name='agni.txt' mode='w' encoding='cp1252'>

print(fp.tell())  # 0
fp.write("Hello! I am Agni Patel!")
print(fp.tell())  # 23
fp.close()

fp = open("agni.txt",'w')
print(fp.tell())  # 0

fp.write("Hello! I am Vishwa Patel!")
print(fp.tell())  # 25
fp.seek(12)
print(fp.tell())  # 13

fp.write("Agni Patel")
print(fp.tell())


list1 = ['Royal is Best Institute Ever\n', 'Ashok is good Boy\n', 'Arvalli Seminar\n']
fp.writelines(list1)

fp.close()

fp1 = open('agni.txt','r')

# print(fp1.readlines())

# print(fp1.read())
print(fp1.readline())  # Hello! I am Agni PatelRoyal is Best Institute Ever
print(fp1.readline())  # Ashok is good Boy
print(fp1.readline())  # Arvalli Seminar

fp1.seek(0)
x = fp1.read()

for t in x:
    print(t)

# Task 
# 1. Starts with 's'
# 2. No. of sentenses, Words, Characters, No of spaces
# 3. Ends with 's'.
# 4. Append Mode



# import pickle ---> load, loads, dump (Explore)

# f = open('','rb')



# for i in fp1:
#     print(i)

# print(fp1)
fp1.close()