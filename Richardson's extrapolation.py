from math import exp,sin
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def richardson_extrapolate(g,h,p):
    #The function g should be made into a function of step size only.
    return ( 2**p * g(h/2) - g(h) )/( 2**p -1)

def derivative_forward_difference(f,x,h):
    return ( f(x+h)-f(x) )/h

def derivative_central_difference(f,x,h):
    return ( f(x+h/2)-f(x-h/2) )/h

def g(x):
    return exp(sin(2*x))

x0 = 0.5
forward_h = lambda h : derivative_forward_difference(g,x0,h)
central_h = lambda h : derivative_central_difference(g,x0,h)

x = sp.symbols('x')
f = sp.exp(sp.sin(2*x))
true_val = sp.diff(f, x).evalf(subs={x: 0.5})

h = 10**-1
h_vals = []
forward_errors = []
central_errors = []

while h>10**-8:
    df = richardson_extrapolate(forward_h,h,1)
    dc = richardson_extrapolate(central_h,h,2)

    # print(f'Forward difference value = {df} , Forward difference error = {abs(df-true_val)}')
    # print(f'Backward difference value = {db} , Backward difference error = {abs(db-true_val)}')
    # print(f'Central difference value = {dc} , Central difference error = {abs(dc-true_val)}')
    # print()

    h_vals.append(h)
    forward_errors.append(abs(df - true_val))
    central_errors.append(abs(dc - true_val))
    h = h/10

plt.plot(-np.log10(h_vals),np.log10(np.array(forward_errors , dtype = float)), marker = "o", label = "Forward difference")
plt.plot(-np.log10(h_vals),np.log10(np.array(central_errors , dtype = float)), marker = "*", label = "Central difference")
plt.legend()
plt.xlabel("-log(h)")
plt.ylabel("log(Error)")
plt.title("Log-log plot showing the variation of error (Richardson's extrapolation)")
plt.show()