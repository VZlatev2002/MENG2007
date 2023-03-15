# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

g = 9.81
L = 0.75

# z = [ thet
#       dthet]

def f(t,z):
    dz = [z[1],
          -g/L*np.sin(z[0])]
    return dz

# Solver params
T = 2
rtol = 1e-6

thet0A = np.linspace(0.4633,0.4635,21)
dthetE = [None]*len(thet0A)

for i, thet0 in enumerate(thet0A):    
    z0 = [thet0*np.pi, 0]

    # IVP solver
    sol = solve_ivp(f, (0,T), z0, rtol=rtol)
    # t = sol.t
    z = sol.y
    # thet = z[0,:]
    dthet = z[1,:]
    
    dthetE[i] = dthet[-1]

fig, ax1 = plt.subplots()
ax1.plot(thet0A,dthetE,'.-')

# 0.4634
