# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:17:10 2017

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
m=47.1 #kg
A=0.51 #m2
Vo=20 #m/s
B=(math.pi/4) #rad
Ch=1.3
p=1.3 #kg/m**3


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
    dvxdt=-(1/2)*p*Ch*(A*senodoa(vx,vy))*(vx**2)*senodoa(vx,vy)/m
    dvydt=-g-(1/2)*p*Ch*(A*senodoa(vx,vy))*(vy**2)*cossdoa(vx,vy)/m
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
    
    
plt.plot(tempo,equacoes[:,2],'r')
plt.ylabel('Velocidade em x(m/s)')
plt.xlabel('tempo(s)')
plt.title('Velocidade em x')
plt.grid(True)
plt.show()

plt.plot(tempo,equacoes[:,3],'r')
plt.ylabel('Velocidade em y(m/s)')
plt.xlabel('tempo(s)')
plt.title('Velocidade em y')
plt.grid(True)
plt.show()


plt.plot(tempo,V,'r')
plt.ylabel('Velocidade(m/s)')
plt.xlabel('tempo(s)')
plt.title('Velocidade total')
plt.grid(True)
plt.show()


plt.plot(equacoes[:,0],equacoes[:,1],'r')
plt.ylabel('Variação da altura(m)')
plt.xlabel('Variação da distância(m)')
plt.axis([0, 40, 0, 12])
plt.grid(True)
plt.title("Descrição da trajetótia de uma pessoa ereta")
plt.show()


import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation

x1 = equacoes[:,0]
y1 = equacoes[:,1]
#parâmetros
rb=0.2
ra=1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 40), ylim=(0, 12))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.5, 0.9, '', transform=ax.transAxes)

barra = patches.Rectangle((0, 0), 0, 0, fc='b')
barra.set_width(rb)
barra.set_height(1.0)

def init():
    ax.add_patch(barra)
    line.set_data([], [])
    time_text.set_text('')
    return line,time_text


def animate(i):
    barra.set_xy([x1[i]-rb/2, y1[i]-1])
    line.set_data(x1[i], y1[i])
    time_text.set_text(time_template % (i*0.01))
    return line,time_text,barra

ani = animation.FuncAnimation(fig, animate,300, interval=25, blit=True, init_func=init)
# ani.save('double_pendulum.mp4', fps=15)
plt.show()