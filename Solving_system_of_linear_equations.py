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
    if not check_lower(A_mat):
        print(f'The input matrix is not lower triangular.')
        exit()
    x_mat = b_mat[:]
    for i in range(len(x_mat)):
        x_mat[i] = (x_mat[i] - sum([A_mat[i][j]*x_mat[j] for j in range(i)]))/A_mat[i][i]
    return x_mat

def backward_substitution(A_mat,b_mat):
    if not check_upper(A_mat):
        print(f'The input matrix is not upper triangular.')
        exit()
    x_mat = b_mat[:]
    for i in range(len(x_mat)-1,-1,-1):
        x_mat[i] = (x_mat[i] - sum([A_mat[i][j]*x_mat[j] for j in range(i+1,len(x_mat))]))/A_mat[i][i]
    return x_mat
    
def gauss_elimination(A_mat,b_mat):
    if np.shape(A_mat)[0]!=np.shape(b_mat)[0]:
        print(f"A and b matrix dimensions don't match.")
        exit()
    n = np.shape(A_mat)[0]
    aug_A = np.zeros((n,n+1))
    for i in range(n):
        aug_A[i] = np.concatenate(( A_mat[i] , np.array([b_mat[i]]) ))
    for i in range(len(A_mat)):
        for j in range(i+1,n):
            aug_A[j] = aug_A[j] - (aug_A[j][i]/aug_A[i][i])*aug_A[i]
    A_new = np.triu(aug_A[:,:n])
    b_new = aug_A[:,n:]
    b_new = b_new.flatten()
    return backward_substitution(A_new,b_new)


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
