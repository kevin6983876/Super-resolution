import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



"""
def rsEGFP(y, t, b, c):
    # on'(t) = -k+*on(t)+k-*off(t)
    # off'(t) = k+*on(t)-k-*off(t)
    # Let y be the vector [on, off].
    on, off = y
    # a system of first order equations
    dydt = [-k_p*on + k_m*off, k_p*on-k_m*off]
    return dydt
k_p = 0.5
k_m = 0
y0 = [0.4, 0.5]
# We will generate a solution at 101 evenly spaced 
# samples in the interval 0 <= t <= 10.
t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(rsEGFP, y0, t, args=(k_p, k_m))
import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'r', label='on(t)')
plt.plot(t, sol[:, 1], 'b', label='off(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("rsEGFP")  
"""

# Reading experimental data as lists
raw_data_PBS = []
with open("PBS.txt") as f:
    for line in f:
        for word in line.split():
            raw_data_PBS.append(float(word)) 

PBS = {}
species_names = ['time','intensity','time2','intensity2']
for name in species_names:
    PBS[name] = []
for i in range(int(len(raw_data_PBS)/2)):
    if i < 500:
        PBS['time'].append(raw_data_PBS[2*i])
        PBS['intensity'].append(raw_data_PBS[2*i+1])
    else:
        PBS['time2'].append(raw_data_PBS[2*i])
        PBS['intensity2'].append(raw_data_PBS[2*i+1])

plt.plot(PBS['time'], PBS['intensity'], 'r', label='PBS(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.savefig("PBS.png") 

raw_data_PA_PBS = []
with open("PA+PBS.txt") as f:
    for line in f:
        for word in line.split():
            raw_data_PA_PBS.append(float(word)) 

PA_PBS = {}
for name in species_names:
    PA_PBS[name] = []
for i in range(int(len(raw_data_PA_PBS)/2)):
    if i < 500:
        PA_PBS['time'].append(raw_data_PA_PBS[2*i])
        PA_PBS['intensity'].append(raw_data_PA_PBS[2*i+1])

raw_data_PA_FC = []
with open("PA+FC.txt") as f:
    for line in f:
        for word in line.split():
            raw_data_PA_FC.append(float(word)) 

PA_FC = {}
for name in species_names:
    PA_FC[name] = []
for i in range(int(len(raw_data_PA_FC)/2)):
    PA_FC['time'].append(raw_data_PA_FC[2*i])
    PA_FC['intensity'].append(raw_data_PA_FC[2*i+1])