#A program to compute and print characteristics of a toy computer.

class ToyComputer:
    def __init__(self,total_bits,exp_bits,significant_bits,bias,exponents = []):
        if exp_bits+significant_bits+1 !=total_bits:
            print(f'ERROR : The number of bits does not match. Number of bits for significant and exponent should add up to one less than the number of total bits.')
            exit()

        self.total_bits = total_bits
        self.exp_bits = exp_bits
        self.significant_bits = significant_bits
        self.bias = bias
        if exponents == []:
            self.exponents = [*range(0,2**(exp_bits)-1)]
        else:
            self.exponents = exponents

        largest_normal_num = 1
        largest_subnormal_num = 0        
        for i in range(1,significant_bits+1):
            largest_normal_num += 1/2**i
            largest_subnormal_num += 1/2**i
        self.smallest_normal_number = 2**( min(self.exponents) - self.bias)
        self.largest_normal_number = largest_normal_num*2**( max(self.exponents) - self.bias)
        self.machine_precision = 1/2**significant_bits
        self.smallest_subnormal_number = (1/2**significant_bits)*2**( min(self.exponents) - bias)
        self.largest_subnormal_number = largest_subnormal_num*2**( min(self.exponents) - bias)
        self.data = {}

    def print_characteristics(self):
        print(f' Smallest normal number = {self.smallest_normal_number}')
        print(f' Largest normal number = {self.largest_normal_number}')
        print(f' Machine precision = {self.machine_precision}')
        print(f' Smallest subnormal number = {self.smallest_subnormal_number}')
        print(f' Largest subnormal number = {self.largest_subnormal_number}')
            

Computer1 = ToyComputer(total_bits=7,exp_bits=3,significant_bits=3,bias=2,exponents=[*range(5)])
Computer1.print_characteristics()


