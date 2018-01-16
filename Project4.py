

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from scipy import signal
from scipy.io import wavfile


mpl.interactive(True)

#1

def tfsenyalperiod(N,f,L,senyal):
    
    nom = senyal
    plt.figure(f"Processat funció senyal {senyal}")

    T = 1 / N
    
    fp = -1/(2*T)
    fg = 1/(2*T)
    
    t = np.linspace(0 , L , N , endpoint = False)
    
    tt = np.linspace(fp,fg,N)
    #1.1
    
    if senyal == "quadrat":
        
        senyal = signal.square( 2 * np.pi * f * t)
        
    elif senyal == "serra":
        
        
        
        senyal = signal.sawtooth( 2 * np.pi * f * t)
        
    #1.2
    
    transform = abs(np.fft.fftshift(np.fft.fft(senyal)))
           
    mask = np.zeros(len(tt))
    
    mask [245: 256] = 1
    #1.3
    resultat = transform * mask 
    
    #1.4
    anti = np.fft.ifft(np.fft.ifftshift(resultat))
    
    titles = [f"Senyal {nom} inicial","mòdul TF inicial","mòdul TF filtrada",f"Senyal{nom} filtrat"]
    sets = [senyal,transform,resultat,anti]
    
    xvar = [t,tt,tt,t]
    
    for i in range(4):
        plt.subplot(4,1,i+1)
        plt.plot(xvar[i],np.real(sets[i]) )
        plt.title(titles[i])


tfsenyalperiod(500 ,5 ,1,"quadrat")
tfsenyalperiod(500 ,5 ,1, "serra")

#2

llargada = 2
freq = 440.0

senyal = np.sin(2 * np.pi * freq * np.linspace(0 , llargada , llargada*44100 ))
#diapaso = wavfile.write("prova5.wav",44100,  senyal )


# analitzador gràfic 


N,a = wavfile.read("cello.wav")

b = list(a)

i = 0

b1 = []

while len(b1) < 44100:
    
    if b[i]!=0:
        
        b1.append(b[i])
    i += 1
 

T = 1 / N #en aquesta expressió està implicit que L=1s (ja que L = NT)
    
fp = -1/(2*T)
fg = 1/(2*T)



t = np.linspace(0 , 1 , 44100)
tt = np.linspace(fp,fg,N)


plt.figure("tractament senyal cello")

plt.subplot(2,2,1)
plt.title("senyal original interval 0,01 segons")
plt.plot(t[0:int(0.01*N)],b1[0:int(0.01*N)])



transform = np.fft.fftshift(np.fft.fft(b1[0:N]))



plt.subplot(2,2,3)
plt.plot(tt,abs(transform))
plt.title("mòdul TF original L=1s")
plt.yscale("log")
plt.xlim([0,3000])


# filtratge baixes freqüències 

mask = np.zeros(len(tt))
    
mask [21050: 23050] = 1


tftallada = transform * mask 

plt.subplot(2,2,4)
plt.plot(tt,abs(tftallada))
plt.title("mòdul TF filtrada")
plt.yscale("log")
plt.xlim([0,3000])



anti = np.fft.ifft(np.fft.ifftshift(tftallada))

filtrat = np.asarray(np.real(anti),dtype=np.int16) 
   
plt.subplot(2,2,2)
plt.plot(t[0:int(0.01*N)],filtrat[0:int(0.01*N)])
plt.ylim([-800,300])
plt.title("senyal filtrat interval 0,01")


#cellofiltrat = wavfile.write("cellofiltrat2.wav",N, filtrat)


