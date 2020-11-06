#%%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
from matplotlib import cm
#%%
#2d example to work with
A = np.matrix([[3.0, 2.0], [2.0, 6.0]])
b = np.matrix([[2.0], [-8.0]])
c = 0.0
#%%
#quadratic form, its minimized by the solution to Ax = b
def f(x, A, b, c):
    return float(0.5 * x.T * A * x - b.T * x + c)
# %%
#plot f(x)
def bowl(A, b, c):
    fig = plt.figure(figsize=(10,8))
    qf = fig.gca(projection = '3d')
    size = 20
    x1 = list(np.linspace(-6, 6, size))
    x2 = list(np.linspace(-6, 6, size))
    x1, x2 = np.meshgrid(x1, x2)
    zs = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.matrix([[x1[i,j]], [x2[i,j]]])
            zs[i,j] = f(x, A, b, c)
    qf.plot_surface(x1, x2, zs, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
    fig.show()
    return x1, x2, zs

x1, x2, zs = bowl(A, b, c)
# %%
#contour plot f(x)
def contoursteps(x1, x2, zs, steps=None):
    fig = plt.figure(figsize=(6,6))
    cp = plt.contour(x1, x2, zs, 10)
    plt.clabel(cp, inline=1, fontsize=10)
    if steps is not None:
        steps = np.matrix(steps)
        plt.plot(steps[:,0], steps[:,1], '-o')
    fig.show()

contoursteps(x1, x2, zs)
# %%
#method of conjugate directions
x = np.matrix([[-2.0],[-2.0]])
steps = [(-2.0, -2.0)]
i = 0
imax = 10
eps = 0.01
r = b - A * x
d = r
deltanew = r.T * r
delta0 = deltanew
while i < imax and deltanew > eps**2 * delta0:
    #step in direction of steepest descent
    alpha = float(deltanew / float(d.T * (A * d)))
    x = x + alpha * d
    steps.append((x[0, 0], x[1, 0]))
    #compute residual for next direction
    r = b - A * x
    deltaold = deltanew
    deltanew = r.T * r
    #calculate beta to get the new conjugate direction
    beta = float(deltanew / float(deltaold))
    d = r + beta * d
    i += 1

contoursteps(x1, x2, zs, steps)
# %%
#method of steepedst descent for comparison
x = np.matrix([[-2.0],[-2.0]])
steps = [(-2.0, -2.0)]
i = 0
imax = 10
eps = 0.01
r = b - A * x
delta = r.T * r
delta0 = delta
while i < imax and delta > eps**2 * delta0:
    #how far to move along direction, using expression given in paper
    alpha = float(delta / (r.T * (A * r)))
    #update solution with direction and how far
    x = x + alpha * r
    steps.append((x[0,0], x[1,0]))  # store steps for future drawing
    r = b - A * x
    delta = r.T * r
    i += 1

contoursteps(x1, x2, zs, steps)
# %%
