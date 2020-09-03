#%%

#example function 
def f(x):
    #return x*x*x*x - 2*x*x*x - 4*x*x + 4*x + 4 
    return x*x*x - x*x + 2


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
bisectionMethod(-200, 300, 100,  0.01)
# %%
