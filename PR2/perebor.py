import numpy as np
from math import gcd

def is_simple(matr):

    det = int(round(np.linalg.det(matr))) % 27
    if det == 0 or gcd(det,27)!=1:
        return False 
    return True




def perebor(c, d, g, h):
    a = (9 - 8*c) % 27
    b = (22 - 8*d) % 27
    e = (20 - 24*g) % 27
    f = (9 - 24*h) % 27

    eq5 = (26*(a*e + b*g) + 12*(c*e + d*g)) % 27
    if eq5 != 22:
        return False

    eq6 = (26*(a*f + b*h) + 12*(c*f + d*h)) % 27
    if eq6 != 22:
        return False

    eq7 = (15*(a*e**2 + b*e*g + c*e*f + d*f*g) + 21*(a*e*g + b*g**2 + c*e*h + d*g*h)) % 27
    if eq7 != 0:
        return False

    eq8 = (15*(a*e*f + b*e*h + c*f**2 + d*f*h) + 21*(a*f*g + b*g*h + c*f*h + d*h**2)) % 27
    if eq8 != 12:
        return False
    
    K1 = np.array([[a, b], [c, d]])
    K2 = np.array([[e, f], [g, h]])

    if not(is_simple(K1)) or not(is_simple(K2)):
        return False

    return True


found = False
for c in range(27):
    for d in range(27):
        for g in range(27):
            for h in range(27):
                if perebor(c, d, g, h):
                    a = (9 - 8*c) % 27
                    b = (22 - 8*d) % 27
                    e = (20 - 24*g) % 27
                    f = (9 - 24*h) % 27
                    print(f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}, g={g}, h={h}")
                    found = True
                    