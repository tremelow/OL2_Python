from integrate import *
from numpy import sqrt, pi

def f(t):
    return sqrt(1 - t**2)

t0, tN = 0, 1
Iex = pi/4

def err(methode, N):
    return abs(methode(f, t0, tN, N) - Iex)

delta = 1e-3
print("Nombre de sous-divisions pour une erreur à %1.0e près :" % delta)

N = 1
while err(rectangles, N) > delta:
    N += 1
print("Rect. :  %d" % N)

N = 1
while err(trapezes, N) > delta:
    N += 1
print("Trap. :  %d" % N)

N = 1
while err(simpson, N) > delta:
    N += 1
print("Simp. :  %d" % N)
