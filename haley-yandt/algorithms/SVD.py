#%%
import numpy as np
from numpy.linalg import svd
import math as math
import cmath as cmath
#%%


#Exercises
#1
#a)

#column space is the first r columns of u
#left null space is remaning columns of u (m by m matrix)

#row space is first r columns of v
#null space is remaining columns of v (n by n matrix)

B = np.array([[2, 1, -1], [3, 1, 2]])
B.shape
r = np.linalg.matrix_rank(B)
print("the rank is:" , r)
#column&row space are dimension 2 (same as rank)
#left null space is 0, null space is 1 


#%%
#b)
U, S, V = svd(B)

#calculates generalize inverse of matrix using svd
pseudo = np.linalg.pinv(B)
print(pseudo)

#solve system using pseudo inverse
y = np.array([5, 1])
x = np.matmul(pseudo, y)
print('x is', x)

#c)
#check answer by solving explicitly 
x_check = np.linalg.lstsq(B, y)
print('x_check is', x_check)


#%%
#2
#a)

A = np.array([[2, 1, -1, 3], [-1, 0, 1, -2], [7, 2, -5, 12], [-3, -2, 0, -4], [4, 1, -3, 7]])
A.shape
#%%
U2, S2, V2 = svd(A)
print(A)
rank = np.linalg.matrix_rank(A)
print(rank)

#A has rank 3, so column space is 3, left null is 2
#row space is 3, null space is 2

#%%
#b)
pseudo2 = np.linalg.pinv(A)
print(pseudo2)

#solve system using pseudo inverse
y2 = np.array([5, 1, 0, -2, 6])
x2 = np.matmul(pseudo2, y2)
print('x2 is', x2)


#c)
x_check2 = np.linalg.lstsq(A, y2)
print('x_check2 is', x_check2)


# %%
#3

theta = np.linspace(0, 2*math.pi, 30)
i = cmath.sqrt(1)
print(i)

#%%
z = np.exp(1j*theta)
real = np.real(z)
imag = np.imag(z)
X = np.array([real,imag]) #domain points
m = 1/math.sqrt(2)
l = m*np.array([[1,1],[1,-1]])
q = np.array([[1,0],[0,3]])
A = np.matmul(l, q)
Y = np.matmul(A,X) #image of circle

#%%
t=np.linspace(0,1)
vec1 = np.matmul(np.array([0,0]),(1-t))
vec1.shape
# %%
