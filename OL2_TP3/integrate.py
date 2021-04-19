from numpy import arange, concatenate

"""
    rectangles(f, a, b, N)

Intègre la fonction f entre les points a et b avec N sous-intervalles en
utilisant la méthode des rectangles. On suppose que f fonctionne avec une
entrée vectorielle.
"""
def rectangles(f, a, b, N):
    h = (b-a)/N
    t = concatenate((arange(a,b,h), [b]))
    # arange(a,b,h) fait une discrétisation de [a,b[ avec un pas h
    # (on pourrait faire `arange(a,b+h,h)` mais j'ai eu des problèmes
    # d'arrondis qui faisaient dépasser b...)
    # Sinon, `linspace(a,b,N+1)` fonctionne, si on importe linspace

    I = 0
    for ti in t:
        I += f(ti)
    I *= h

    # Avec sum :
    I = h*sum(f(t))

    return I



def trapezes(f, a, b, N):
    h = (b-a)/N
    t = concatenate((arange(a,b,h), [b]))

    I = 0
    for i in range(N):
        I += f(t[i]) + f(t[i+1])
    I *= 0.5*h

    # Avec sum :
    I = h*sum(f(t)) - 0.5*h * (f(t[0]) + f(t[-1]))

    return I



def simpson(f, a, b, N):
    h = (b-a)/N
    t = concatenate((arange(a,b,h), [b]))

    I = 0
    for i in range(N):
        tm = 0.5 * (t[i] + t[i+1])
        I += f(t[i]) + f(t[i+1]) + 4*f(tm)
    I *= h/6

    # Avec sum :
    tm = 0.5 * (t[1:] + t[:-1])
    I  = h/3 * sum(f(t)) + 2*h/3 * sum(f(tm))
    I -= h/6 * (f(t[0]) + f(t[-1]))

    return I