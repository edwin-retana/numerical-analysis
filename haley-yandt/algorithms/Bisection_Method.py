#%%
import sympy as sym

#%%
#example function 
def f(x):
    return x**3 - 2*x**2 - 5
    #return x*x*x - x*x + 2


def derivative(f, var, n):
    x = sym.symbols('x')
    expr = sym.diff(f, x, n) 
    return expr.subs(x, var)

#%%
#n is number of allowed iterations, t is tolerance 
def bisectionMethod(a, b, n, t):
    i = 1
    fa = f(a)
    while (i <= n):
        if (f(a) * f(b) >= 0):
            print("incorrect inputs, do not return opposite signs")
            return
        p = (a+b)/2
        fp = f(p)
        if ((fp == 0) or ((b-a)/2 < t)):
            print("the root is", p)
            return
        i = i + 1
        if (fa * fp > 0): 
            a = p   
            fa = fp
        else:
            b = p 
    print("method failed")
            
#%%
bisectionMethod(2, 3, 1000,  0.1)
# %%
def NewtonMethod(p_initial, t, n):
    i = 1
    x = sym.symbols('x')
    while (i <= n):
        p = p_initial - (f(p_initial) / derivative(f(x), p_initial, 1))
        p = float(p)
        if (abs(p - p_initial) < t):
            print('the root is', p)
            return 
        i = i + 1
        p_initial = p
    print('method failed, too many iterations')
    return 

NewtonMethod(2, 0.0001, 1000)

#%%
