from math import exp,sin
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def derivative_forward_difference(f,x,h):
    return ( f(x+h)-f(x) )/h

def derivative_backward_difference(f,x,h):
    return ( f(x)-f(x-h) )/h

def derivative_central_difference(f,x,h):
    return ( f(x+h/2)-f(x-h/2) )/h

def g(x):
    return exp(sin(2*x))

x = sp.symbols('x')
f = sp.exp(sp.sin(2*x))
true_val = sp.diff(f, x).evalf(subs={x: 0.5})

h = 10**-1
h_vals = []
forward_errors = []
backward_errors = []
central_errors = []

while h>10**-12:
    df = derivative_forward_difference(g,0.5,h)
    db = derivative_backward_difference(g,0.5,h)
    dc = derivative_central_difference(g,0.5,h)

    # print(f'Forward difference value = {df} , Forward difference error = {abs(df-true_val)}')
    # print(f'Backward difference value = {db} , Backward difference error = {abs(db-true_val)}')
    # print(f'Central difference value = {dc} , Central difference error = {abs(dc-true_val)}')
    # print()

    h_vals.append(h)
    forward_errors.append(abs(df-true_val))
    backward_errors.append(abs(db-true_val))
    central_errors.append(abs(dc - true_val))
    h = h/10

plt.scatter(-np.log10(h_vals),np.log10(np.array(forward_errors , dtype = float)), label = "Forward difference")
plt.scatter(-np.log10(h_vals),np.log10(np.array(backward_errors , dtype = float)), label = "Backward difference")
plt.scatter(-np.log10(h_vals),np.log10(np.array(central_errors , dtype = float)), label = "Central difference")
plt.legend()
plt.xlabel("-log(h)")
plt.ylabel("log(Error)")
plt.title("Log-log plot showing the variation of error with step size.")
plt.show()
