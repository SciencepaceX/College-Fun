import numpy as np, random as rd, matplotlib.pyplot as plt, math as mt,sympy as sp
from Funcy import DP,TrapezoidalIntegral,F_interpolate

t = sp.Symbol('t')
a_t_values = [DP(0,0), DP(1,1), DP(2,4), DP(3,7), DP(4,9), DP(5,15), DP(6,17)]
a_values = [a_t_values[i].b for i in range(0,7)]
t_values = [a_t_values[i].a for i in range(0,7)]

a = F_interpolate(a_t_values,7,t)
v_values = [0]
v_i = 0
for i in range(0,6):
    v_i += TrapezoidalIntegral(a,i,i+1,100,t)
    v_values.append(v_i)

print(v_values)
plt.subplot(1,2,1)
plt.plot(t_values,a_values,color="g")
plt.scatter(t_values,a_values)
plt.xlabel("Time")
plt.ylabel("Acceleration/Velocity")
plt.title("A-T Graph")
plt.grid()
plt.subplot(1,2,2)
plt.plot(t_values,v_values,color="m")
plt.scatter(t_values,v_values,color= "k")
plt.xlabel("Time")
plt.ylabel("Acceleration/Velocity")
plt.title("A-T Graph")
plt.grid()
plt.show()





