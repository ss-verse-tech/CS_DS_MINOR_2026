# class Bird:
#     def __init__(self, name, color, wings_color):
#         self.name = name
#         self.color = color
#         self.wings_color = wings_color
#         print("Constructor is calling")

#     @staticmethod #it is known as decorator
#     def fly():
#         return f"Bird can fly"

# b1 = Bird("Sparrow", "Brown", "black")
# b2 = Bird("cockoo", "black", "black")

# # print(Bird.fly())
# print(b1.fly())
# print(b2.fly())

# Abstraction
# Show functionality hide complexity

# class Car:
#     def __init__(self):
#         acc = False
#         brk = False
#         gear = False
#         clutch = False

#     def start(self):
#         acc = True
#         gear = True
#         clutch = True
#         if(acc == True and gear == True and clutch == True):
#             return "Car is starting"
#         else:
#             return "Car is not starting"

# c1 = Car();
# c2 = Car()
# c3 = Car()
# print(c1.start())