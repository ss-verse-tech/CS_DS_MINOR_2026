# variable length positional argument

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


#     def sum(self, *args):
#         return sum(args)

#     def subtract(self, *args):
#         return args


# s1 = Student("Mohit", 30)
# print(s1.sum(2,3,4))
# print(s1.sum(10,20))
# print(s1.subtract(6,4,2))

# Operator overloading
# Build In Datatypes
# print(2+2)
# print(int.__add__(2,2))
# print(str.__add__("2", "5"))

# user_defined_Data_type

class Number:
    def __init__(self, value):
        self.value = value

    # __add__ dunder function/magic function

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value-other.value
    

n1 = Number(5)
n2 = Number(3)
n3 = Number(6)

print(n1 + n2+n3)
