# Вычислить число Пи c заданной точностью d
# Пример:

#     - при d = 0.0001,  π = 3.1415    10^-1 ≤ d ≤10^-10

a = 355
b = 113
d = 0.0001

def f_pi(x, y):
    result_f_pi = x/y
    return result_f_pi

p = f_pi(a, b)

def f_len(h,m):
    s = len(str(p)) - (len(str(p)) - len(str(d)))
    return s

def f_limit_pi():
    res = str(p)[0:f_len(p,d)]
    return res

print(f_limit_pi())