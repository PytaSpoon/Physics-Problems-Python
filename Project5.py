# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:33:01 2017

@author: Pere Lopez
"""
from pylab import *
import csv, operator
from scipy.integrate import simps
from scipy.integrate import quad


lamb= []
x = []
y = []
z = []
E = []

with open ('arxiu_problema.csv') as arxiu:
    linies=arxiu.read().splitlines()
    for l in linies:
        linia = l.split(" ")
        lamb.append(float(linia[0]))
        x.append(float(linia[1]))
        y.append(float(linia[2]))
        z.append(float(linia[3]))
        E.append(float(linia[4]))

figure('Distribucions triestímul i Energia')
subplot(1,2,1); plot(lamb,x, label='x'); plot(lamb,y, label='y'); plot(lamb,z,label='z')
ylabel('Nombre del valor'); xlabel('Longitud de ona'); axis([380,650,0,2]); legend() 
title("Distribucions triestímuls respecte lambda")
subplot(1,2,2); plot(lamb,E, label='E'); title("Energia respecte lambda")
axis([380,650,0,2]); legend()
#fx = lambda x: E*x
#fy = lambda y: E*y
#fz = lambda z: E*z

yx = []
yy = []
yz = []
for i in range (len(E)):
    ix = E[i]*x[i] ; yx.append(ix)
    iy = E[i]*y[i] ; yy.append(iy)
    iz = E[i]*z[i] ; yz.append(iz)
 

linf = 380
lsup = 650

#varx = quad(fx,linf,lsup)
#vary = quad(fy,linf,lsup)
#varz = quad(fz,linf,lsup)

varx2 = simps(yx,lamb)
vary2 = simps(yy,lamb)
varz2 = simps(yz,lamb)

#Generalització de coordenades
suma = varx2 + vary2 + varz2
X = varx2 / suma
Y = vary2 / suma
Z = varz2 / suma

xyz = array([[X],[Y],[Z]])

p1 = [3.240479, -1.537150, -0.498535]
p2 = [-0.969256, 1.875992, 0.041556]
p3 = [0.055648, -0.204043, 1.057311]
mg = array([p1,p2,p3])

rgb = dot(mg, xyz)

N = 250
c1 = ones([N,N,3])

c1[:,:,0]=rgb[0][0]
c1[:,:,1]=rgb[1][0]
c1[:,:,2]=rgb[2][0]

figure('Color 1')
imshow(c1)

# Per E=1
E=1

fx = lambda x: E*x
fy = lambda y: E*y
fz = lambda z: E*z

varx = quad(fx,linf,lsup)
vary = quad(fy,linf,lsup)
varz = quad(fz,linf,lsup)

suma = varx[0] + vary[0] + varz[0]
X = varx[0] / suma
Y = vary[0] / suma
Z = varz[0] / suma

xyz = array([[X],[Y],[Z]])  

rgb = dot(mg, xyz)

c1 = ones([N,N,3])
c1[:,:,0]=rgb[0][0]
c1[:,:,1]=rgb[1][0]
c1[:,:,2]=rgb[2][0]

figure('Color 2')
imshow(c1)