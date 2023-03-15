# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import solve_ivp
from Pendulum_Animations import animate_pendulum

g = 9.81
L = 0.75

# z = [ thet
#       dthet]

def f(t,z):
    dz = [z[1],
          -g/L*np.sin(z[0])]
    return dz

def my_event(t,z):
    return np.pi/4 - z[0]
my_event.terminal = True
my_event.direction = +1

# Solver params
T = 10
rtol = 1e-6
z0 = [np.pi/2, 0]

# IVP solver
sol = solve_ivp(f, (0,T), z0, rtol=rtol, events=my_event)
t = sol.t
z = sol.y
thet = z[0,:]

ani = animate_pendulum(t,thet)

