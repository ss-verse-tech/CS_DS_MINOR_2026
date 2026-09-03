# from multipledispatch import dispatch
# EXAMPLE OF POLYMORPHISM
# class Cat:
#     def sound(self):
#         return "Cat can meow"

# class Dog(Cat):
#     def sound(self):
#         return "Dog can bark"

# d = Dog();
# print(d.sound())


# class Calculation:
#     @dispatch(int, int)
#     def add(self, a,b):
#         return a+b
    
#     @dispatch(int, int, int)
#     def add(self, a,b,c):
#             return a+b+c

# c = Calculation()
# print(c.add(2,4))
# print(c.add(2,4,5))
