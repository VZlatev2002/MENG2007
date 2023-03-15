# -*- coding: utf-8 -*-

import numpy as np
from scipy.integrate import solve_ivp
# from Pendulum_Animations import animate_sprung_pendulum
import matplotlib.pyplot as plt

m = 1
g = 9.81
L = 0.75
k = 50
c = 1
Ls = 0.5
Ld = 0.6

def f(t,z):
    dz = [z[1],
          -g/L*np.sin(z[0])]
    return dz

def f_C(t,z):
    dz = [z[1],
          -g/L*np.sin(z[0]) - Ls**2*k/(m*L**2)*z[0] - Ld**2*c/(m*L**2)*z[1]]
    return dz

def my_event(t,z):
    return z[0]
my_event.terminal = True

# Solver params
T = 10
rtol = 1e-6
IC = [np.pi/2, 0]

# IVP solver
my_event.direction = -1
sol0 = solve_ivp(f, (0,T), IC, rtol=rtol, events=my_event)
t0 = sol0.t
z0 = sol0.y
thet0 = z0[0,:]

IC = sol0.y[:,-1]
my_event.direction = +1
sol1 = solve_ivp(f_C, (t0[-1],t0[-1]+T), IC, rtol=rtol, events=my_event)
t1 = sol1.t
z1 = sol1.y
thet1 = z1[0,:]

IC = sol1.y[:,-1]
my_event.direction = -1
sol2 = solve_ivp(f, (t1[-1],t1[-1]+T), IC, rtol=rtol, events=my_event)
t2 = sol2.t
z2 = sol2.y
thet2 = z2[0,:]

IC = sol2.y[:,-1]
my_event.direction = +1
sol3 = solve_ivp(f_C, (t2[-1],t2[-1]+T), IC, rtol=rtol, events=my_event)
t3 = sol3.t
z3 = sol3.y
thet3 = z3[0,:]

IC = sol3.y[:,-1]
my_event.direction = -1
sol4 = solve_ivp(f, (t3[-1],t3[-1]+T), IC, rtol=rtol, events=my_event)
t4 = sol4.t
z4 = sol4.y
thet4 = z4[0,:]

IC = sol4.y[:,-1]
my_event.direction = +1
sol5 = solve_ivp(f_C, (t4[-1],t4[-1]+T), IC, rtol=rtol, events=my_event)
t5 = sol5.t
z5 = sol5.y
thet5 = z5[0,:]

# t = np.concatenate((t0,t1,t2,t3,t4,t5))
# thet = np.concatenate((thet0,thet1,thet2,thet3,thet4,thet5))

# ani = animate_sprung_pendulum(t,thet)

fig, ax1 = plt.subplots()

ax1.plot(t0,thet0,'b')
ax1.plot(t1,thet1,'r')
ax1.plot(t2,thet2,'b')
ax1.plot(t3,thet3,'r')
ax1.plot(t4,thet4,'b')
ax1.plot(t5,thet5,'r')

ax1.set_xlabel(r'$t\;[s]$')
ax1.set_ylabel(r'$\theta\;[rad]$')

print(t5[-1])
