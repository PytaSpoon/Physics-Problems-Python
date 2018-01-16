# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:26:06 2017

@author: fis.aules
"""

"""Pèndol simple"""

from pylab import *
from scipy.integrate import odeint

# Pèndol esmorteït

#Definim la funció amb les equacions del pèndol esmorteit i forçat
def pendolesm(y,t):
    """ Condicions inicials:
    y[0]=velocitat ; y[1]=angle
    """
    return (-g*sin(y[1])/L+(-b*y[0]+a*cos(om*t))/m*L**2), y[0]

#Opció A
#definim les condicions inicials
t = linspace(0,12,1000); g=9.81; L=1
a = 0; b = 0; om = 0; L = 1; m = 0.15
ci2 = array([0,pi/10])
#creem una variable amb la resolució de la integral
fpe=odeint(pendolesm,ci2,t)

#com que ho torna en forma de columnes, recollim els resultats en 2 variables
angle2 = fpe[:,1]
velocitat2 = fpe[:,0]
#representem els resultats en dos gràfics en la mateixa finestra
figure("""Pendol esmorteït""")
subplot(1,2,1); plot(t,angle2); title("Representació de l'angle")
subplot(1,2,2); plot(t,velocitat2); title("Representació de la velocitat")

#Opció B

#Afegim una nova condició i tornem a integrar i recollir els resultats
b=0.05
fpe2 = odeint(pendolesm, ci2,t)
angle3 = fpe2[:,1]
velocitat3 = fpe2[:,0]

#Ho grafiquem de la mateixa manera que abans
figure("""Pendol esmorteit 2""")
subplot(1,2,1); plot(t,angle3); title("Representació de l'angle")
subplot(1,2,2); plot(t,velocitat3); title("Representació de la velocitat")

#Opció C

#Definim unes terceres condicions inicials
a = 1.35 ;m = 1 ;g = 1 ;L = 1 ;b = 0.5 ;om = 0.666 ;t2 = linspace(0,60,2000)

#Integrem i recollim els resultats en noves variables
fpe3 = odeint(pendolesm, ci2, t2)
angle4 = fpe3[:,1]
velocitat4 = fpe3[:,0]

#Gràfiquem els resultats com anteriorment ho hem fet
figure("""Pendol esmorteit i forçat""")
subplot(1,2,1); plot(t2,angle4); title("Representació de l'angle")
subplot(1,2,2); plot(t2,velocitat4); title("Representació de la velocitat")

#Pendols acoblats:

#Definim una nova funció per als pèndols acoblats
def pendolaco(y,t):
    """ y[0]=v1 ; y[1]=v2 ; y[2]=x1 ; y[3]=x2
    retorna: x'1, x'2, v'1, v'2"""
    return (k2*y[3]-(k1+k2)*y[2])/m, (k2*y[2]-(k1+k2)*y[3])/m, y[0], y[1]

#definim unes noves condicinos inicials
m = 1; k1 = 10; k2 = 0.5
ya = array([0,0,1,0])
ta = linspace(0,40,1000)

#integrem i recollim els resultats que les col·loquem en diferents variables
faco = odeint(pendolaco,ya,ta)
v1 = faco[:,0]
v2 = faco[:,1]
x1 = faco[:,2]
x2 = faco[:,3]

#Representem els gràfics amb les corresponents característiques
figure("Acoblats")
subplot(1,2,1); plot(ta,x1,label="Pèndol 1"); plot(ta,x2,label="Pèndol 2") 
title("Posició de la partícula")
xlabel("Temps(s)"); ylabel("Posició de la partícula")
grid(True)
legend()
subplot(1,2,2); plot(ta,v1,label="Pèndol 1"); plot(ta,v2,label="Pèndol 2")
title("Velocitat respecte el temps")
xlabel("Temps(s)"); ylabel("Velocitat partícula")
grid(True)
legend()

#Gravitació

#Definim una nova funció per al moviment gravitatori
def campgrav(c,t):
    """ Condicions inicials:
    c[0]=vx c[1]=vy c[2]=x c[3]=y """
    vx = -(G*Mt*c[2])/((c[2]**2+c[3]**2)**1.5)
    vy = -(G*Mt*c[3])/((c[2]**2+c[3]**2)**1.5)
    x = c[0]
    y = c[1]
    return vx,vy,x,y

G = 6.67e-11 #Nm^2/kg^2

#Dades del Sol
Mt = 2e30 #kg
tg = linspace(0,3.16e7,100000)
cg = array([29800,0,0,1.5e11])

#integrem i recollim els resultats que les col·loquem en diferents variables
calcg = odeint (campgrav, cg, tg)
vx = calcg[:,0]
vy = calcg[:,1]
vt = (vx**2+vy**2)**0.5
x = calcg[:,2]
y = calcg[:,3]

#Representem els gràfics amb les corresponents característiques
figure("Estudi de la Terra")
subplot(2,2,1);plot(tg,x);title("X vs T")
subplot(2,2,2);plot(tg,y);title("Y vs T")
subplot(2,2,3);plot(x,y);title("Òrbita");axis("equal")
subplot(2,2,4);plot(tg,vt);title("Velocitat de translació")


#Dades del Halley
Mt = 1.989e30 #kg
per= 75.316*365.25*24*3600
th = linspace(0,per,5e4)
axi = 0.586*149597870700
vh = 54561.5
ch = array([0,vh,-(axi),0])

#integrem i recollim els resultats que les col·loquem en diferents variables
calch = odeint (campgrav, ch, th)
xh = calch[:,2]
yh = calch[:,3]
vxh = calch[:,0]
vyh = calch[:,1]
vth = (vxh**2+vyh**2)**0.5

#Representem els gràfics amb les corresponents característiques
figure("Estudi del cometa Halley")
subplot(2,2,1);plot(th,xh);title("X vs T")
subplot(2,2,2);plot(th,yh);title("Y vs T")
subplot(2,2,3);plot(xh,yh);title("Òrbita");axis("equal")
subplot(2,2,4);plot(th,vth);title("Velocitat de translació")






















