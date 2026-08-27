# Multiple Inheritance
# class Parent:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def play(self):
#         return f"{self.name} can play"
# class Child:
#     def __init__(self, eye_color):
#         self.eye_color = eye_color
#     def dance(self):
#         return f"child can dance"
# class Subchild(Parent, Child):
#     def __init__(self, name , age, eye_color, hair_color):
#         self.hair_color = hair_color
#         Parent.__init__(self,name, age)
#         Child.__init__(self,eye_color)

#     def cook(self):
#         return f"{self.name} can cook"


# s = Subchild("Mohit", 4, "black","Brown")
# print(s.name)

#  Keyword Argument
# class Parent:
#     def __init__(self, name , age , **kwargs):
#         self.name = name
#         self.age = age
#         super().__init__(**kwargs)

#     def play(self):
#         return f"{self.name} can play"
# class Child:
#     def __init__(self, eye_color, **kwargs):
#         self.eye_color = eye_color
#         super().__init__(**kwargs)

#     def dance(self):
#         return f"child can dance"
    
# class Subchild(Parent, Child):
#     def __init__(self, name , age, eye_color, hair_color):
#         self.hair_color = hair_color
#         # Parent.__init__(self,name, age)
#         # Child.__init__(self,eye_color)
#         super().__init__(name=name,age=age,eye_color=eye_color)

#     def cook(self):
#         return f"{self.name} can cook"


# s = Subchild("Mohit", 4, "black","Brown")
# print(s.name)



# # creating MRO (Method Resolution Order)
# class A:
#     def play(self):
#         return "A can play"

# class B(A):
#     def sing(self):
#         return "B can sing"

# class C(B,A):
#     def dance(self):
#         return "C can dance"


# c = C()
# print(c.play())