#Method 1(BY USING INBUILT FUNCTION):
 
print("Format for writing complex number: a+bj.\n")
c1 = complex(input("Enter First Complex Number: "))
c2 = complex(input("Enter second Complex Number: "))
print("Sum of both the Complex number is", c1 + c2)
print("Subtraction of both the Complex number is", c1 - c2)

#Method 2(BY USING USER DEFINED FUNCTION):

class Complex ():
    def initComplex(self):
        self.realPart = int(input("Enter the Real Part: "))
        self.imgPart = int(input("Enter the Imaginary Part: "))            
    def display(self):
        print(self.realPart,"+",self.imgPart,"i", sep="")
    def sum(self, c1, c2):
        self.realPart = c1.realPart + c2.realPart
        self.imgPart = c1.imgPart + c2.imgPart
    def sub(self, c1, c2):
        self.realPart = c1.realPart - c2.realPart
        self.imgPart = c1.imgPart - c2.imgPart    
c1 = Complex()
c2 = Complex()
c3 = Complex()
print("Enter first complex number")
c1.initComplex()
print("First Complex Number: ", end="")
c1.display()
print("Enter second complex number")
c2.initComplex()
print("Second Complex Number: ", end="")
c2.display()
print("Sum of two complex numbers is ", end="")
c3.sum(c1,c2)
c3.display()
print("Difference of two complex numbers is ", end="")
c3.sub(c1,c2)
c3.display()