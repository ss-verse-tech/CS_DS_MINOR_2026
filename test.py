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
#         return f"{self.name} can dance"

# class SubChild(Parent, Child):
#     def __init__(self, name , age, eye_color,hair_color):
#         self.hair_color = hair_color
#         # super().__init__(name , age)
#         # super().__init__(eye_color)
#         Parent.__init__(self,name, age)
#         Child.__init__(self,eye_color)

#     def sing(self):
#         return f"{self.name} can sing"


# s1 = SubChild("Mohit", 40, "black", "brown")
# print(s1.name)







class Parent:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)

    def play(self):
        return f"{self.name} can play"


class Child:
    def __init__(self, eye_color, **kwargs):
        self.eye_color = eye_color
        super().__init__(**kwargs)

    def dance(self):
        return f"{self.name} can dance"


class SubChild(Parent, Child):
    def __init__(self, name, age, eye_color, hair_color):
        self.hair_color = hair_color

        super().__init__(name=name,age=age,eye_color=eye_color)

    def sing(self):
        return f"{self.name} can sing"


s1 = SubChild("Mohit", 40, "black", "brown")

print(s1.name)
print(s1.age)
print(s1.eye_color)
print(s1.hair_color)

print(s1.play())
print(s1.dance())
print(s1.sing())


