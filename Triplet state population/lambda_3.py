import numpy as np

P_origin=0.000002

sigma=1.3*10**(-20)
P=P_origin*2.58*10**(18)
omega_1=0.24*10**(-6)
k_12=sigma*P/np.pi/omega_1**2
k_21=250000000
k_23=900000
k_31=500000

lambda_3 = -k_31-k_12*k_23/(k_12+k_21)
print(lambda_3/1000000)