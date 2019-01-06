# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 18:05:31 2018

@author: Pere Lopez
"""
from pylab import *
from scipy import integrate as inte

v0=10
f0=50
p=1/f0
t=linspace(v0,v0+p,1000)

def vt(t):
    """ simplement el voltatge"""
    return v0*sin(2*pi*f0*t)

def vr(t):
    """ voltatge rectificat """
    return 10*abs(sin(100*pi*t))

def va(t,n):
    """ an a integrar """
    return vt(t)*cos(2*pi*n*t/p)*2/p

def vb(t,n):
    """ bn a integrar """
    return vt(t)*sin(2*pi*n*t/p)*2/p

an=[]
bn=[]
n_it=[]

for i in range(30):
    a,a1=inte.quad(va,v0,v0+p,i)
    b,b1=inte.quad(vb,v0,v0+p,i)
    an.append(a)
    bn.append(b)
    n_it.append(i)
dades = vstack((n_it,an,bn))
dades = dades.T
savetxt('Dades.txt',dades,fmt='%d\t%.4e\t%.4e', header='N\t\tAn\t\tBn')

def va2(t,n):
    """ an a integrar """
    return vr(t)*cos(2*pi*n*t/p)*2/p

def vb2(t,n):
    """ bn a integrar """
    return vr(t)*sin(2*pi*n*t/p)*2/p

s=[]
a2=[]
b2=[]
eps=[]

for i in range(5):
        a,a1=inte.quad(va2,v0,v0+p,i)
        b,b1=inte.quad(vb2,v0,v0+p,i)
        a2.append(a)
        b2.append(b)

ser = a2[0]/2

for x in t:
    for i in range(1,4):
        ser = ser + a2[i]*cos(2*pi*x*i/p) + b2[i]*sin(2*pi*x*i/p)
    s.append(ser)
    e = abs(vt(x)-ser)
    eps.append(e)
    ser=a2[0]/2

figure('1')
subplot(211)
plot(t, vr(t), 'y+', lw = 0.75, label = 'Vr(t)')
plot(t, s, 'g-', lw = 0.75, label = 's(t)')
subplot(212)
plot(t, eps, lw = 0.75)

error=1
i=0
ea=an[0]**2/2
def vtt(t):
    """ simplement el voltatge"""
    return (v0*sin(2*pi*f0*t))**2
 



    

    