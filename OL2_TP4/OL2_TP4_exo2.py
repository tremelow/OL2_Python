from numpy import *
from matplotlib.pyplot import *


R, C, V = 1e3, 1e-3, 10

def f(t,q):
    return -q/(R*C) + V/R

def sol_ex(t):
    return V*C*(1.0 - exp(-t/(R*C)))

def euler(y0, t0, tN, N):
    h = (tN - t0)/N
    t = linspace(t0, tN, N+1)
    
    y = [y0]
    for n in range(N):
        y.append(y[n] + h*f(t[n], y[n]))
        
    return t,y

y0, t0, tN = 0.0, 0.0, 5.0
for N in [5, 10, 20, 50]:
    t, y  = euler(y0, t0, tN, N)
    scatter(t, y, label="N = " + str(N), marker="x")

t_ex = linspace(t0, tN, 201)
y_ex = sol_ex(t_ex)
plot(t_ex, y_ex, label="sol. ex.", color="purple")
legend()