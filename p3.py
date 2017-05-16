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
tempo=np.arange(0,4,0.1)
#cd 0.70 a 50000
#cd=24/re
g=10 #m/s2
m=20 #kg
A=math.pi*(0.15**2) #m2
Vo=20 #m/s
B=(math.pi/4) #rad
Cx=1
p=1.3 #kg/m**3


def Fr(v):
    r=(1/2)*p*Cx*A*(v**2)
    return r

def senodoa(vx,vy):
    s=vy/((vx**2+vy**2)**(1/2))
    return s

def cossdoa(vx,vy):
    c=vx/((vx**2+vy**2)**(1/2))
    return c
    
              

def eq(Y,tempo):
    x=Y[0]
    y=Y[1]
    vx=Y[2]
    vy=Y[3]
    dxdt=vx
    dydt=vy
    dvxdt=-Fr(vx)*cossdoa(vx,vy)
    dvydt=-g-Fr(vy)*senodoa(vx,vy)/m
    return [dxdt,dydt,dvxdt,dvydt]



C0=[0,0,Vo*math.cos(B),Vo*math.sin(B)]
equacoes=odeint(eq,C0,tempo)
#plt.plot(equacoes[:,2],equacoes[:,3])
#plt.ylabel('dvydt')
#plt.xlabel('dvxdt')
#plt.grid(True)
#plt.show()


plt.plot(equacoes[:,0],equacoes[:,1])
plt.ylabel('Variação da altura(m)')
plt.xlabel('Variação da distância(m)')
plt.axis([0, 25, 0, 12])
plt.grid(True)
plt.title("Descrição da trajetótia de uma esfera")
plt.show()