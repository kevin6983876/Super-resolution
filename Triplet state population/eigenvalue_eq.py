import numpy as np
from numpy.linalg import eig
import math

def norm_X_t(X_0, P_origin,t):
    sigma=1.3*10**(-20)
    P=P_origin*2.58*10**(18)
    omega_1=0.24*10**(-6)
    k_12 = sigma*P/np.pi/omega_1**2
    k_21=25000000
    k_23=900000
    k_31=500000
    A = np.array([[-k_12,  k_21,  k_31],
              [k_12,  -(k_23+k_21),  0],
              [0,  k_23,  -k_31]])
    w,v=eig(A) #v: eigenvector is at each column
    v_inv = np.linalg.inv(v)
    C = np.matmul(v_inv,X_0)
    C_t = np.array([C[0]*math.exp(w[0]*t),C[1]*math.exp(w[1]*t),C[2]*math.exp(w[2]*t)])
    X_t = np.matmul(v,C_t)
    return X_t/np.linalg.norm(X_t)

T_eq1 = []
T_eq2 = []
#T_eq3 = []

time = np.linspace(1,10000,10000)
for i in range(100):
    T_eq1.append(norm_X_t(np.array([1,0,0]),0.00002,0.000000001*i)[2])
#for i in range(1000):
#    T_eq2.append(norm_X_t(np.array([1,0,0]),0.00002,0.000000001*i)[2])
#for i in range(10000):
#    T_eq3.append(norm_X_t(np.array([1,0,0]),0.00002,0.000000001*i)[2])
Turn_off1 = norm_X_t(np.array([1,0,0]),0.00002,0.000000199)
#Turn_off2 = norm_X_t(np.array([1,0,0]),0.00002,0.000001999)
#Turn_off3 = norm_X_t(np.array([1,0,0]),0.00002,0.000019999)
for i in range(9900):
    T_eq1.append(norm_X_t(Turn_off1,0,0.000000001*i)[2])
#for i in range(99000):
#    T_eq2.append(norm_X_t(Turn_off2,0,0.000000001*i)[2])
#for i in range(90000):
#    T_eq3.append(norm_X_t(Turn_off3,0,0.000000001*i)[2])
import matplotlib.pyplot as plt
plt.plot(time/1000,T_eq1, label='0.1us dwell time')
#plt.plot(time/1000,T_eq2, label='1us dwell time')
#plt.plot(time/1000,T_eq3, label='10us dwell time')
plt.legend(loc='best')
plt.ylabel("Relative triplet state population")
plt.xlabel("time(us)")
plt.savefig("T_eq") 

