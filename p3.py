# -*- coding: utf-8 -*-
"""
Created on Tue May 16 07:35:34 2017

@author: milen
"""
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

tempo=np.arange(0,1000,0.1)
#cd 0.70 a 50000
#cd=24/re
g=10
m=20 #kg
A=math.pi*(0.15**2) #m2
Vo=20 #m/s
B=(math.pi/4) #rad
Cx=0.7
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
    dvxdt=-Fr(vx)*senodoa(vx,vy)
    dydt=vy
    dvydt=g+ Fr(vy)*cossdoa(vx,vy)/m
    if vx==vy:
        vy=-vy
    return [dxdt,dydt,dvxdt,dvydt]

C0=[0,0,Vo*math.cos(B),Vo*math.sin(B)]
equacoes=odeint(eq,C0,tempo)
plt.plot(equacoes[:,0],equacoes[:,1],'c')
plt.ylabel('dydt')
plt.xlabel('dxdt')
plt.grid(True)
plt.show()