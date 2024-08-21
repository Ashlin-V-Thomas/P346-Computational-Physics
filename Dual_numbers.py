# Description: This file contains the class Dual_Number, which is used to represent dual numbers and perform arithmetic operations on them.
class Dual_Number:
    def __init__(self, real, dual):
        self.real = real
        self.dual = dual
    
    def __add__(self, other):
        return Dual_Number(self.real + other.real, self.dual + other.dual)
    
    def __sub__(self, other):
        return Dual_Number(self.real - other.real, self.dual - other.dual)
    
    def __mul__(self, other):
        return Dual_Number(self.real * other.real, self.real * other.dual + self.dual * other.real)
    
    def __truediv__(self, other):
        return Dual_Number(self.real / other.real, (self.dual * other.real - self.real * other.dual) / other.real**2)
    
    def __pow__(self, n):
        return Dual_Number(self.real**n, n*self.real**(n-1)*self.dual)
    
    def print(self):
        print( f"{self.real} + {self.dual}d" )
    
f_dual = lambda x : (x-Dual_Number(2,0))*(x - Dual_Number(3,0))/(x-Dual_Number(4,0))

f_dual(Dual_Number(6,1)).print() # The real component of output is the value of the function at x=6 and the dual component is the derivative of the function at x=6.
    

        

