# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:36:01 2017

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
w=3#rad/s

def senodoa(vx,vy):
    s=vx/((vx**2+vy**2)**(1/2))
    return s

def cossdoa(vx,vy):
    c=vy/((vx**2+vy**2)**(1/2))
    return c
              
def senodeao(vx,vy,tempo):
    s=senodoa(vx,vy)*(np.cos(w*tempo))-(np.sin(w*tempo))*cossdoa(vx,vy)
    return s

def cossdeao(vx,vy,tempo):
    c=cossdoa(vx,vy)*np.cos(w*tempo)+senodoa(vx,vy)*np.sin(w*tempo)
    return c
    
    

def eq(Y,tempo):
    x=Y[0]
    y=Y[1]
    vx=Y[2]
    vy=Y[3]
    dxdt=vx
    dydt=vy
    dvxdt=-(1/2)*p*Ch*(A*senodeao(vx,vy,tempo))*(vx**2)*senodeao(vx,vy,tempo)/m
    dvydt=-g-(1/2)*p*Ch*(A*senodeao(vx,vy,tempo))*(vy**2)*cossdeao(vx,vy,tempo)/m
    return [dxdt,dydt,dvxdt,dvydt]



C0=[0,0,Vo*math.cos(B),Vo*math.sin(B)]
equacoes=odeint(eq,C0,tempo)
VX=[]
VY=[]

for i in equacoes[:,0]:
    VX.append(i)
    
for i in equacoes[:,1]:
    VY.append(i)

V=[]
for i in range(len(VX)):
    a=((VX[i]**2)+(VY[i]**2))**(1/2)
    V.append(a)
    
    
plt.plot(tempo,equacoes[:,0])
plt.ylabel('Velocidade de x')
plt.xlabel('tempo')
plt.grid(True)
plt.show()

plt.plot(tempo,equacoes[:,1])
plt.ylabel('Velocidade de y')
plt.xlabel('tempo')
plt.grid(True)
plt.show()


plt.plot(tempo,V)
plt.ylabel('Velocidade')
plt.xlabel('tempo')
plt.grid(True)
plt.show()

plt.plot(equacoes[:,0],equacoes[:,1])
plt.ylabel('Variação da altura(m)')
plt.xlabel('Variação da distância(m)')
plt.axis([0, 40, 0, 12])
plt.grid(True)
plt.title("Descrição da trajetótia de uma pessoa ereta rotacionando")
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


barra = patches.Rectangle((0, 0), 0, 0, fc='b')
barra.set_width(rb)
barra.set_height(1.0)

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 40), ylim=(0, 12))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.5, 0.9, '', transform=ax.transAxes)


def init():
    ax.add_patch(barra)
    line.set_data([], [])
    time_text.set_text('')
    return line,time_text,barra

def animate(i):
    barra.set_xy([x1[i]-rb/2, y1[i]-1])
    line.set_data(x1[i], y1[i])
    time_text.set_text(time_template % (i*0.01))
    return line,time_text,barra


ani = animation.FuncAnimation(fig, animate,300, interval=25, blit=True, init_func=init)
plt.show()