# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

from __future__ import division, print_function

from pylab import *

#Generarem el conjunt de punts del conjunt de Mandelbrot per a calcular 
#aquells punts que formen el fractal.
X,Y = meshgrid(linspace(-2,1,500),linspace(-1.5,1.5,500))

#generem la matriu de punts imaginaris C
c=X+1j*Y

#z=0 es la condició inicial
z=0

#Creem una matriu de zeros amb el mateix tamany per a poder calcular les 
#velocitats de convergencia.
M=zeros((500,500))

#Generem les dos figures on es mostraran els fractals
f1=figure("Conjunt de mandelbrot")
f2=figure("Velocitat de convergencia de Mandelbrot")

#Fem un bucle for per a generar imatges depenent de la iteracio
for i in range (12):
    z = z**2 + c
    z[(z.real**2+z.imag**2)**0.5 > 10**40]=2 + 3*1j #aplicant la formula
    
    zz = abs(z) < 2 #creem la matriu dels booleans dins del sistema
    
    cm = double(zz) #els representem amb nombres
    
    M = M + cm  #fem un contador per saber les velocitats de convergencia
    
    #a partir d'aquí el codi és nomes per afegir els grafics
    acm=f1.add_subplot(3,4,i+1)
    acm.imshow(cm,cmap='gray')     
    acm.axis('off')
    am=f2.add_subplot(3,4,i+1)
    am.imshow(M,cmap='gist_rainbow')     
    am.axis('off')

#Escrivim el terme que conforma el conjunt de Julia
t=-0.7269 + 0.1889*1j

#Afegim un rang mes ampli per a mostrar correctament el conjunt
X,Y = meshgrid(linspace(-2,2,750),linspace(-1.5,1.5,500))

#Creem la matriu dels punts imaginaris
c=X+1j*Y
fs=c

#Creem una altre matriu de zeros
J=zeros((500,750))

#Generem dues finestres per a obrir els dos nous grafics
f3=figure("Conjunt de Julia")
f4=figure("Velocitat de convergencia de Julia")


#Tornem a fer un bucle for per a calcular els conjunts segons la iteracio
for i in range (12):
    fs = fs**2 + t #Usem la formula
    fs[(fs.real**2+fs.imag**2)**0.5 > 10**40]=2 + 3*1j #Apliquem una condició
                                                       #Per evitar nans
    fz = abs(fs) < 2 #Creem la matriu de booleans
    
    cj = double(fz) #Generem una matriu de nombres dels booleans
    
    J = J + cj #Fem la suma de les matrius per aconseguir la velocitat de conv
    
    #a partir d'aquí el codi és nomes per afegir els gràfics
    acm2=f3.add_subplot(3,4,i+1)
    acm2.imshow(cj,cmap='gray')     
    acm2.axis('off')
    am2=f4.add_subplot(3,4,i+1)
    am2.imshow(J,cmap='rainbow')     
    am2.axis('off')
