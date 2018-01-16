# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

# Entrega 3

from pylab import *

# Tasca 1
# creem una funció que retorni l'index de refracció respecte lambda
# depenent del rang de longituds i del material que nosaltres volguem

def ns(x,nom):
    """nom és el nom del material, x és la longitud d'ona"""
    di = {'vidre' : 1, 'diòxid de titani' : 2, 'fluorur de magnesi' : 3}
    # creem un diccionari per a optar els 3 diferents materials
    if di[nom] == 1:
        n=(1+1.03961212/(1-0.00600069867/x**2)+0.231792344/(1-0.0200179144/x**2)+1.01046945/(1-103.560653/x**2))**.5
        return n
    if di[nom] == 2:
        n=(5.913+0.2441/(x**2-0.0803))**.5
        return n
    if di[nom] == 3:
        n=(1+0.48755108/(1-(0.04338408/x)**2)+0.39875031/(1-(0.09461442/x)**2)+2.3120353/(1-(23.793604/x)**2))**.5
        return n

# la següent funció retorna l'index respecte lambd
def indref(nom,li,lf):
    """nom és el nom del material, x és la long d'ona,
    li la longitud inicial i lf la longitud final"""
    x = linspace(li,lf,1000) #rang de longituds d'ona 
    n = ns(x,nom)
    return n

# creo les diferents variables amb els corresponents índexs
v = indref('vidre', 0.3, 1.1)
t = indref('diòxid de titani', 0.3, 1.1)
f = indref('fluorur de magnesi', 0.3, 1.1)
x = linspace(0.3,1.1,1000)
figure('Index de refracció')
plot(x,v,label="BK7");plot(x,t,label="TiO2");plot(x,f,label="MgF2");legend()

# Tasca 2

# creo dues funcions, una retorna el gruix de la capa, i l'altra la matriu de matrius
# de la capa per les longituds d'ona
def dtreb(ltreb,nom):
    """ltreb és la longitud d'ona de treball i n és 
    el nom del material"""
    dtr = ltreb/(4*ns(ltreb,nom))
    return dtr

def M (dt,n,l):
    """funció de creació de la matriu M cal aportar
    l'index de refracció, la longitud d'ona de la capa, i el gruix dt"""
    # cada p[num] és una component de la matriu
    p1 = cos((2*pi/l)*n*dt)
    p2 = (1j/n)*sin((2*pi/l)*n*dt)
    p3 = (1j*n)*sin((2*pi/l)*n*dt)
    p4 = p1
    mm=[]
    for i in range (1000):
        m = array([[p1[i],p2[i]],[p3[i],p4[i]]])
        mm.append(m)
    return mm

# Tasca 3
# creem 3 matrius per a veure com actua un sistema de dos capes
dt1 = dtreb(0.7,'diòxid de titani')
m1 = M(dt1,t,x)

dt2 = dtreb(0.7,'fluorur de magnesi')
m2 = M(dt2,f,x)

dt3 = dtreb(0.7,'vidre')
m3 = M(dt3,v,x)

mt = []
bc = []
rlam = []
n0 = 1
ns = 1.52

# fem un bucle for amb la formula que ens aporta per a calcular la
# reflactancia i la transmitància

for i in range (len(m1)):
    mp = dot(m1[i],m2[i])
    mt.append(mp)
    nn = array([[n0],[ns]])
    dx = dot(mt[i],nn)
    bc.append(dx)
    num = n0*bc[i][0][0]-bc[i][1][0]
    den = n0*bc[i][0][0]+bc[i][1][0]
    r = num/den
    rlam.append(r)

rdef = (abs(array(rlam)))**2
tdef = ones(1000) - rdef

#figure("Grafica 2")
#plot(x,rdef);plot(x,tdef)
# Part 4

# tornem a fer un sistema de 3 capes però ara el vidre depen de lambda
nn2 = []
bc2 = []
rlam = []
n0 = 1
ns = v

# fem un bucle for amb la formula que ens aporta per a calcular la
# reflactancia i la transmitància
for i in range (len(m1)):
    nn2.append([[n0],[ns[i]]])
    mtx = dot(mt[i],nn2[i])
    bc2.append(mtx)
    num = n0*bc2[i][0][0]-bc2[i][1][0]
    den = n0*bc2[i][0][0]+bc2[i][1][0]
    r = num/den
    rlam.append(r)
    
rdef2 = (abs(array(rlam)))**2
tdef2 = ones(1000) - rdef2
#figure("Grafica 3")
#plot(x,rdef2);plot(x,tdef2) 

# Tasca 5
# creem ara una funció que usarem per a crear totes les capes del sistema

def mbloc2(ncapes,mt,m1,m2):
    Mtc = mt
    for i in range(ncapes-2):
        
        if i%2==0:
            
            Mtc = [dot(Mtc[j],m1[j]) for j in range(len(Mtc))]
            
        elif i%2 != 0:
            
            Mtc = [dot(Mtc[j],m2[j]) for j in range(len(Mtc))]        
    return Mtc
    

ncap = 20

mtt = mbloc2(ncap,mt,m1,m2)

nn3 = []
bc3 = []
rlam = []
n0 = 1
ns = 1.52

# tornem a generar el mateix bucle for per a recollir les dades del nou sistema multicapes

for i in range (len(mtt)):
    nn3 = array([[n0],[ns]])
    mtx = dot(mtt[i],nn3)
    bc3.append(mtx)
    num = n0*bc3[i][0][0]-bc3[i][1][0]
    den = n0*bc3[i][0][0]+bc3[i][1][0]
    r = num/den
    rlam.append(r)
    
rdef3 = (abs(array(rlam)))**2
tdef3 = ones(len(rdef3)) - rdef3
x = linspace(0.3,1.1,len(rdef3))
figure("Sistema multicapes de 20 capes")
plot(x,rdef3,label="R");plot(x,tdef3,label="T") 
legend()

    
















