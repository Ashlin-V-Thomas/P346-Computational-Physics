import numpy as np
from tabulate import tabulate


def eig_val_power(A_mat, x_guess = None, max_operations = 200, tolerance = 10**-6):
    n = np.shape(A_mat)[0]
    if x_guess == None:
        x = np.random.rand(n)
        x = x/np.linalg.norm(x)
    else:
        x = x_guess/np.linalg.norm(x_guess)
    val_old = None
    for op in range(max_operations):
        x = A_mat@x
        x = x/np.linalg.norm(x)
        if val_old == None:
            val_old = x.T@A_mat@x
            continue
        val_new = x.T@A_mat@x
        if abs((val_old-val_new)/val_new)<tolerance:
            print(f'The eigenvalue converged within the mentioned tolerance after {op} iterations.')
            return val_new
        val_old = val_new
    print(f"The dominant eiegenvalue didn't converge within the tolerance of {tolerance} even after {max_operations} iterations.")
    return


mat1 = np.random.rand(4,4)
print(f"The input matrix A = \n {tabulate(mat1,tablefmt= "grid")}")
print(f"The dominant eigenvalue computed using inbuilt numpy function = {np.linalg.eig(mat1)[0][0]}.")
print(f"The dominant eigenvalue computed using power method = {eig_val_power(mat1)}")
