# class Complex_number:
#     def __init__(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self, other):
#         return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"


# c1 = Complex_number(2,5)
# c2 = Complex_number(6,7)
# print(c1+c2)



class Complex_number:
    def __init__(self, real):
        self.real = real

    def extract(self, str):
        arr = []
        for i in str:
            # print(i)
            if(i.isdigit()):
                i = int(i)
                arr.append(i)
        return arr

    def __add__(self, other):
        # return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
        return f"{self.extract(self.real)[0]+ self.extract(other.real)[0]} +  {self.extract(self.real)[1] + self.extract(other.real)[1]}i"


c1 = Complex_number("70+6i")
c2 = Complex_number("9+8i")
print(c1+c2)