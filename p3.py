# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:35:34 2017

@author: milen
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 
#cd homem ereto 1.3
#cd cabeca 2
tempo=np.arange(0,4,0.01)
#cd 0.70 a 50000
#cd=24/re
g=10 #m/s2
m=6 #kg
A=math.pi*(0.15**2) #m2
Vo=20 #m/s
B=(math.pi/4) #rad
Cx=0.7
p=1.3 #kg/m**3


def Fr(v):
    r=(1/2)*p*Cx*A*(v**2)
    return r

def senodoa(vx,vy):
    s=vx/((vx**2+vy**2)**(1/2))
    return s

def cossdoa(vx,vy):
    c=vy/((vx**2+vy**2)**(1/2))
    return c
    
              

def eq(Y,tempo):
    x=Y[0]
    y=Y[1]
    vx=Y[2]
    vy=Y[3]
    dxdt=vx
    dydt=vy
    dvxdt=-Fr(vx)*senodoa(vx,vy)/m
    dvydt=-g-Fr(vy)*cossdoa(vx,vy)/m
    return [dxdt,dydt,dvxdt,dvydt]



C0=[0,0,Vo*math.cos(B),Vo*math.sin(B)]
equacoes=odeint(eq,C0,tempo)


VX=[]
VY=[]

for i in equacoes[:,2]:
    VX.append(i)
    
for i in equacoes[:,3]:
    VY.append(i)

V=[]
for i in range(len(VX)):
    a=((VX[i]**2)+(VY[i]**2))**(1/2)
    V.append(a)
    
    
plt.plot(tempo,equacoes[:,2])
plt.ylabel('Velocidade em x(m/s)')
plt.xlabel('tempo(s)')
plt.title('Velocidade em x')
plt.grid(True)
plt.show()

plt.plot(tempo,equacoes[:,3])
plt.ylabel('Velocidade em y(m/s)')
plt.xlabel('tempo(s)')
plt.title('Velocidade em y')
plt.grid(True)
plt.show()


plt.plot(tempo,V)
plt.ylabel('Velocidade(m/s)')
plt.xlabel('tempo(s)')
plt.title('Velocidade total')
plt.grid(True)
plt.show()

plt.plot(equacoes[:,0],equacoes[:,1])
plt.ylabel('Variação da altura(m)')
plt.xlabel('Variação da distância(m)')
plt.axis([0, 40, 0, 12])
plt.grid(True)
plt.title("Descrição da trajetótia de uma esfera")
plt.show()


import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

x1 = equacoes[:,0]
y1 = equacoes[:,1]


fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 40), ylim=(0, 12))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.5, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line,time_text


def animate(i):
    line.set_data(x1[i], y1[i])
    time_text.set_text(time_template % (i*0.01))
    return line,time_text

ani = animation.FuncAnimation(fig, animate,300, interval=25, blit=True, init_func=init)
plt.show()