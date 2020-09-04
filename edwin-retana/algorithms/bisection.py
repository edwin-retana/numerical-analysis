#Edwin Retana
#MATH 481 - Numerical Analysis in Python
#Sep. 3, 2020

def f(x):
    return x*x + 4*x - 1
#x^2 + 4x - 1
#zero's @ x = -4.236068, 0.23606798

def sign(val):
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0

#We assume going in that a and b are different signs.
def bisection_solution(a, b, tol, n):
    if sign(f(a)) == sign(f(b)):
        print('Invalid pair for \'a\' and \'b\'.')
    i = 1
    f_a = f(a)
    while i <= n:
        p = a + (b-a)/2
        f_p = f(p)
        if f_p == 0 or (b-a)/2 < tol:
            print(p)
            return
        i = i + 1
        if f_a*f_p > 0:
            a = p
            f_a = f_p
        else:
            b = p
    print('Method failed after ' + str(n) + ' iterations.')

a_test_1 = -10
b_test_1 = 0
a_test_2 = -2
b_test_2 = 4
n_test = 1000
tol_test = 0.00001
bisection_solution(a_test_1, b_test_1, tol_test, n_test)
bisection_solution(a_test_2, b_test_2, tol_test, n_test)
