import numpy as np
from tabulate import tabulate

def condition_number(A):
    A_inv = np.linalg.inv(A)
    return np.linalg.norm(A)*np.linalg.norm(A_inv)

def check_lower(inmat):
    for i in range(len(inmat)):
        for j in range(i+1,len(inmat)):
            if inmat[i][j] !=0:
                return False
    return True

def check_upper(inmat):
    for i in range(len(inmat)):
        for j in range(i):
            if inmat[i][j] !=0:
                return False
    return True

def forward_substitution(A_mat, b_mat):
    n = len(b_mat)
    if not check_lower(A_mat):
        print(f'The input matrix is not lower triangular.')
        exit()
    x_mat = np.zeros(n)
    for i in range(len(x_mat)):
        x_mat[i] = (b_mat[i] - sum([A_mat[i][j]*x_mat[j] for j in range(i)]))/A_mat[i][i]
    return x_mat

def backward_substitution(A_mat,b_mat):
    n = len(b_mat)
    if not check_upper(A_mat):
        print(f'The input matrix is not upper triangular.')
        exit()
    x_mat = np.zeros(n)
    for i in reversed(range(n)):
        x_mat[i] = (b_mat[i] - sum([A_mat[i][j]*x_mat[j] for j in range(i+1,len(x_mat))]))/A_mat[i][i]
    return x_mat


def gauss_elimination(A_mat,b_mat):
    if np.shape(A_mat)[0]!=np.shape(b_mat)[0]:
        print(f"A and b matrix dimensions don't match.")
        exit()
    n = np.shape(A_mat)[0]
    A = np.copy(A_mat)
    b = np.copy(b_mat)

    for i in range(n-1):
        for j in range(i+1,n):
            coeff  = A[j][i]/A[i][i]
            A[j,i:] = A[j,i:] - coeff*A[i,i:]
            b[j] = b[j] - coeff*b[i]
    
    return backward_substitution(np.triu(A),b)

def gauss_elimination_partial_pivot(A_mat,b_mat):
    if np.shape(A_mat)[0]!=np.shape(b_mat)[0]:
        print(f"A and b matrix dimensions don't match.")
        exit()
    n = np.shape(A_mat)[0]
    A = np.copy(A_mat)
    b = np.copy(b_mat)

    for i in range(n-1):
        m = np.argmax([A[i:,i]]) + i
        A[i],A[m] = A[m].copy(),A[i].copy()
        b[i],b[m] = b[m],b[i]
        for j in range(i+1,n):
            coeff  = A[j][i]/A[i][i]
            A[j][i:] = A[j][i:] - coeff*A[i][i:]
            b[j] = b[j] - coeff*b[i]
    
    return backward_substitution(np.triu(A),b)

def gauss_elimination_scaled_partial_pivot(A_mat,b_mat):
    if np.shape(A_mat)[0]!=np.shape(b_mat)[0]:
        print(f"A and b matrix dimensions don't match.")
        exit()
    n = np.shape(A_mat)[0]
    A = np.copy(A_mat)
    b = np.copy(b_mat)

    row_scale_factors = np.array([np.max(A[i]) for i in range(len(A))])
    A_temp = A/row_scale_factors[:,None]
    for i in range(n-1):
        m = np.argmax(A_temp[i:,i])+i
        A[i],A[m] = A[m].copy(),A[i].copy()
        b[i],b[m] = b[m],b[i]
        for j in range(i+1,n):
            coeff  = A[j][i]/A[i][i]
            A[j][i:] = A[j][i:] - coeff*A[i][i:]
            b[j] = b[j] - coeff*b[i]
    
    return backward_substitution(np.triu(A),b)

def LU_decompose(A_mat,b_mat):
    n = np.shape(A_mat)[0]
    L = np.eye(n)
    U = np.copy(A_mat)
    for i in range(n-1):
        for j in range(i+1,n):
            coeff = U[j][i]/U[i][i]
            L[j][i] = coeff
            U[j][i:] = U[j][i:] - coeff*U[i][i:]
    return backward_substitution(np.triu(U),forward_substitution(L,b_mat))

def jacobi_iteration(A_mat,b_mat,tolerance = 10**-6, x_start = None, max_iterations = 100):
    n = np.shape(A_mat)[0]
    if x_start == None:
        x_start = np.random.rand(n)
    
    for k in range(max_iterations):
        x_new = np.zeros(n)
        for i in range(n):
            x_new[i] = (b_mat[i] - A_mat[i,:i]@b_mat[:i] - A_mat[i,i+1:]@b_mat[i+1:])/A_mat[i,i]
        if np.sum(np.abs((x_new-x_start)/x_new))<= tolerance:
            return x_new
        x_start = x_new
    print(f"The jacobi iterative method didn't converge even after {max_iterations} iterations." )
    exit()

mat1 = np.random.rand(4,4)
mat1_lower = np.tril(mat1)
mat1_upper = np.triu(mat1)
b = np.random.rand(4)

print(f'A-matrix - ')
print(tabulate(mat1,tablefmt='grid'))
print(f"Condition number = {condition_number(mat1)}")
print()

print(f'b-matrix = {b} ')
print()

print(f'The solution of the system with the coefficient matrix being lower triangular part of A.')
print(f'Output of inbuilt numpy function = {np.linalg.solve(mat1_lower,b)}')
print(f'Output of forward substitution method = {forward_substitution(mat1_lower,b)}')
print()

print(f'The solution of the system with the coefficient matrix being upper triangular part of A.')
print(f'Output of inbuilt numpy function = {np.linalg.solve(mat1_upper,b)}')
print(f'Output of backward substitution method = {backward_substitution(mat1_upper,b)}')
print()

print(f'The solution of the system with the coefficient matrix being A.')
print(f'Output of inbuilt numpy function = {np.linalg.solve(mat1,b)}')
print(f'Output of gauss elimination method = {gauss_elimination(mat1,b)}')
print(f'Output of gauss elimination method with partial pivotting = {gauss_elimination_partial_pivot(mat1,b)}')
print(f'Output of gauss elimination method with scaled partial pivotting = {gauss_elimination_partial_pivot(mat1,b)}')
print(f'Output of LU decomposition method = {LU_decompose(mat1,b)}')
print()

print(f'The solution of the system with the coefficient matrix being a diagonal matrix with the main diagonal of A.')
print(f'Output of inbuilt numpy function = {np.linalg.solve(np.diag(np.diag(mat1)),b)}')
print(f'Output of jacobi iterative method = {jacobi_iteration(np.diag(np.diag(mat1)),b)}')