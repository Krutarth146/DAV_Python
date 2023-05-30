str1 = "Royal_Is Best Institute Ever123."

print(len(str1))  # 32  length starts from 1, index starts from 0


str2 = '500'
print(str2.zfill(5)) # 00500

print(str1.upper())  # ROYAL_IS BEST INSTITUTE EVER123.
print(str1.lower())  # royal_is best institute ever123.
print(str1.casefold())  # royal_is best institute ever123.
print(str1.swapcase())  # rOYAL_iS bEST iNSTITUTE eVER123.
print(str1.capitalize())  # Royal_is best institute ever123.
print(str1.title())  # Royal_Is Best Institute Ever123.
print(str1.isupper())  # False
print(str1.islower())  # False
print(str1.istitle())  # True

str1 = "RoyalIsBestInstituteEver"
print(str1.isalpha())  # True
print(str1.isspace())  # False
print(str1.isalnum())  # True


str4 = "5673"
print(str4.isdecimal())  # True
print(str4.isdigit())  # True
print(str4.isnumeric())  # True


str1 = "Royal_Is Best Institute Ever123."
print(str1.center(32))  # Royal_Is Best Institute Ever123.
print(str1.center(36))  #   Royal_Is Best Institute Ever123.
print(str1.center(41,'*'))  # *****Royal_Is Best Institute Ever123.****
 
print(str1.ljust(40,'*'))  # Royal_Is Best Institute Ever123.********
print(str1.rjust(40,'*'))  # ********Royal_Is Best Institute Ever123.


print(str1.split(' '))  # ['Royal_Is', 'Best', 'Institute', 'Ever123.']
print(str1.partition(' '))  # ('Royal_Is', ' ', 'Best Institute Ever123.')  # Total 3 Parts only
print(str1.rpartition(' '))  # ('Royal_Is Best Institute', ' ', 'Ever123.')  # Total 3 Parts only

str1 = "Royal_Is Best Institute Ever123."
str1 = str1.replace('tute', 'moon')
# str1 = str1.replace('e', 'o')
str1 = str1.replace('e', 'o', 1)
print(str1)



# Task
# oye balle balle oye
# OyE BallE BallE OyE

# agni AgnI


# str1 = "Vishwa"
# print(id(str1))
# print(str1[3]) # h
# # str1[3] = 'D'

# str2 = "Patel"
# str1 += str2
# print(id(str1))
# print(str1)