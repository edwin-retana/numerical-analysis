#%%

import numpy as np
import numpy.linalg 
from matplotlib import pyplot as plt 
#%%

#2
#numpy has a function, numppy.vander that generates 
#a vandermonde matrix, the columns of the output matrix
#are powers of the input vector. The order is determined
#by the increasing boolean argument, so for the matrix to match 
#our definition it would be np.vander(x, increasing=True).
#By default, square matrix is returned but can also change number of columns


#Example:
x = np.array([1,2,3,5])
np.vander(x, increasing=True)

#%%
#3
def fun(x):
    return (1/(1+12*x**2))
#Example 1, 7 points
#First define the points for the polynomial:
xp = np.linspace(-1, 1, 7)
yp = fun(xp)

#Find the coefficients using the Vandermonde matrix
V = np.vander(xp)
C = np.linalg.solve(V, yp)

xx = np.linspace(-1,1,200)
#function data
yy1 = fun(xx)
#model data 
yy2 = np.polyval(C, xx)
#%%
plt.plot(xp, yp, marker='*')
plt.plot(xx, yy1)
plt.plot(xx, yy2)
plt.legend(['Data', 'f(x)', 'Polynomial'])
plt.title('Interpolation using 7 points, Degree 6 poly')
plt.show()

#%%
#Example 2, 15 points
xp2 = np.linspace(-1, 1, 15)
yp2 = fun(xp2) 

V2 = np.vander(xp2)
C2 = np.linalg.solve(V2, yp2)

xx2 = np.linspace(-1, 1, 200)
yy3 = fun(xx2)
yy4 = np.polyval(C2, xx2)

#%%
plt.plot(xp2, yp2, marker='*')
plt.plot(xx2, yy3)
plt.plot(xx2, yy4)
plt.legend(['Data', 'f(x)', 'Polynomial'])
plt.title('Interpolation using 15 points, Degree 14 poly')
plt.show()


#%%  
#Example 3, 30 points, degree 9: 

xp3 = np.linspace(-1, 1, 30)
yp3 = fun(xp3)

V3 = np.vander(xp3, N=10)

#returns solution, sum, rank, and singular values of V3, but we just need the solution
solution = np.linalg.lstsq(V3, yp3)
C3 = solution[0]

xx3 = np.linspace(-1, 1, 200)
yy5 = fun(xx3)
yy6 = np.polyval(C3, xx3)

#%%
plt.plot(xp3, yp3, marker='*')
plt.plot(xx3, yy5)
plt.plot(xx3, yy6)
plt.legend(['Data', 'f(x)', 'Polynomial'])
plt.title('Interpolation using 30 points, Degree 10 poly')
plt.show()
#%%