str1 = "R"
print(type(str1))

str2 = "Royal_is Best Institute Ever123."

print(str2)

# char name[10] = "Manoj";  # Mutable
# name[2] = 'k';

# string is Immutable (Unchangeble)

print(id(str2))  # 1853489156368
print(str2.__sizeof__())   # 81
print(len(str2))   # 32  ---> Length starts from 1

str3 = "ROyal"

print(id(str3))    # 1425712034672
# str4 = "Institute"
str3 += " Vishwa "  # 1425712092016
print(id(str3))
print(str3)  # ROyal Vishwa

# str3[2] = "M"  # TypeError: 'str' object does not support item assignment

# Indexing
str2 = "Royal_is Best Institute Ever123."
print(str2[0])  # R
print(str2[-1])  # .
print(str2[-3])  # 2
print(str2[-7])  # 2

# Slicing

# print(str1[start : end(n-1) : step (n-1)])
str2 = "Royal_is Best Institute Ever123."
print(str2[0:10]) # Royal_is B
print(str2[2:])  # yal_is Best Institute Ever123.
print(str2[:4])  # Roya
print(str2[:])  # Royal_is Best Institute Ever123.
print(str2[7:2])   # 
print(str2[-2:2])  # 
print(str2[-2:2:1])  # 
print(str2[-2:2:-1])  #  # 321revE etutitsnI tseB si_la
print(str2[::1])  #  Royal_is Best Institute Ever123.
print(str2[::-1])  #  .321revE etutitsnI tseB si_layoR
print(str2[::-2])  #  .2rv tttn sBs_ao
print(str2[:4:])  #  Roya
print(str2[:-4:])  #  Royal_is Best Institute Ever
print(str2[::])  #  Royal_is Best Institute Ever123.
print(str2[:-6:-3])  #  .1
print(str2[-4:3:2])  #  blank