import numpy as np

def rsEGFP(y, t, b, c):
    # on'(t) = -k+*on(t)+k-*off(t)
    # off'(t) = k+*on(t)-k-*off(t)
    # Let y be the vector [on, off].
    on, off = y
    # a system of first order equations
    dydt = [-k_p*on + k_m*off, k_p*on-k_m*off]
    return dydt
k_p = 0.5
k_m = 0.5
y0 = [0.4, 0.5]
# We will generate a solution at 101 evenly spaced 
# samples in the interval 0 <= t <= 10.
t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(rsEGFP, y0, t, args=(k_p, k_m))
import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='on(t)')
plt.plot(t, sol[:, 1], 'g', label='off(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()