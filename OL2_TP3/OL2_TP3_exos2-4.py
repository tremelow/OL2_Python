from numpy import *
from matplotlib.pyplot import *

def f(t):
    return sqrt(1 - t**2)

def rectangles(N):
    h = 1/N
    t = arange(0,1+h,h)
    # arange(a,b,h) fait une discrétisation de [a,b[ avec un pas h

    I = 0
    for ti in t:
        I += f(ti)
    I *= h

    # Avec sum :
    I = h*sum(f(t))

    return I

def trapezes(N):
    h = 1/N
    t = arange(0,1+h,h)

    I = 0
    for i in range(N):
        I += f(t[i]) + f(t[i+1])
    I *= 0.5*h

    # Avec sum :
    I = h*sum(f(t)) - 0.5*h * (f(t[0]) + f(t[-1]))

    return I

def simpson(N):
    h = 1/N
    t = arange(0,1+h,h)

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

Iex = pi/4
N = 20
I1 = rectangles(N)
I2 = trapezes(N)
I3 = simpson(N)

print("Erreur rectangles : " + str(abs(Iex - I1)))
print("Erreur trapezes : " + str(abs(Iex - I2)))
print("Erreur Simpson : " + str(abs(Iex - I3)))