# def union(A, B):
#     A = A.union(B)    
#     return sorted(A)



# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# a = set(a)
# b = set(b)
# res = union(a,b)
# print(res)


# ------------------------------------------------------

# Structure  ---> User Defined Datatype

# class Student
# {
#     int id;
#     char name[10];
#     float marks;

#     void set_data()
#     {
#         id = 90;
#         marks = 900;
#     }

#     void display()
#     {
#         cout<<id<<marks<<name;
#     }
# };
# struct College
# {
#     int id;
#     char name[10];
#     float marks;
# };
# struct School
# {
#     int id;
#     char name[10];
#     float marks;
# };



# main()
# {
#              int     a;
#     struct Student s1
#            Student s2;
# }

# class --> Blueprint of object
# object --> Instance of class


# Constructor ----> TO intialize Member Variable
# Student()
# {

# }

# Self == this 


class Student:
    ROI = 5   # Class Variable

    # def __init__(self):
    #     self.id = 10     # Instance Variable
    #     self.name = "sdcscs"        # Instance Variable
    #     self.marks = 12121  # Instance Variable
    def __init__(self, id, name, marks):
        self.id = id     # Instance Variable
        self.name = name        # Instance Variable
        self.marks = marks  # Instance Variable

# Magic methods

# Student s1;   in CPP
dev = Student(10, "Zafar Sir", 900)
vishwa = Student(30, 'Shrey Sir', 800)


print(dev.id)  # 10
print(vishwa.marks)  # 800

print(dev.ROI)   # 5
print(vishwa.ROI)   #  5
print(Student.ROI)   #  5
# print(Student.id)   #  5   Gives Error

# Student.ROI = 90


# print(dev.ROI)   # 90
# print(vishwa.ROI)   #  90
# print(Student.ROI)   #  90

dev.ROI = 93

  
print(dev.ROI)   # 90   # Instance Variable
print(vishwa.ROI)   #  5   # static Variable
print(Student.ROI)   #  5   # Static Variable

dev.friends = 25

print(dev.friends)   # 25
# print(vishwa.friends)   # 25  # Gives Error