from integrate import * # module local (l'autre fichier)
from numpy import sqrt, pi # module installé (numpy)

def f(t):
    return sqrt(1 - t**2)


t0, tN = 0, 1
tab_N = [10,20,50,100,200,300]
I_rect = [0 for _ in tab_N]
I_trap = [0 for _ in tab_N]
I_simp = [0 for _ in tab_N]

for (i,N) in enumerate(tab_N):
    I_rect[i] = rectangles(f, t0, tN, N)
    I_trap[i] = trapezes(f, t0, tN, N)
    I_simp[i] = simpson(f, t0, tN, N)


print("   N  :    ", end="")
print(*[" %3d     " % N for N in tab_N], sep="")
print("Rect. :    ", end="")
print(*["%1.3f    " % I_N for I_N in I_rect], sep="")
print("Trap. :    ", end="")
print(*["%1.3f    " % I_N for I_N in I_trap], sep="")
print("Simp. :    ", end="")
print(*["%1.3f    " % I_N for I_N in I_simp], sep="")
