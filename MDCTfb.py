#Functions to implement the complete MDCT filter bank. File based, it first reads in the complete audio file and then computes the MDCT filter bank output.
#Gerald Schuller, August 2017.


from DCT4 import *
from symFmatrix import symFmatrix
from Dmatrix import Dmatrix  
from polmatmult import polmatmult 
from x2polyphase import *
def MDCTanafb(x,N,fb):
   #MDCT analysis filter bank.
   #Arguments: x: input signal, e.g. audio signal, a 1-dim. array
   #N: number of subbands
   #fb: coefficients for the MDCT filter bank, for the F matrix, np.array with 1.5*N coefficients.
   #returns y, consisting of blocks of subband in in a 2-d array of shape (N,# of blocks)
   
   Fa=symFmatrix(fb)
   D=Dmatrix(N)
   y=x2polyphase(x,N)
   y=polmatmult(y,Fa)   
   y=polmatmult(y,D)
   y=DCT4(y)
   #strip first dimension:
   y=y[0,:,:]
   return y
   
from Dinvmatrix import Dinvmatrix
from polyphase2x import *   
def MDCTsynfb(y,fb):
   #MDCT synthesis filter bank.
   #Arguments: y: 2-d array of blocks of subbands, of shape (N, # of blokcs)
   #returns xr, the reconstructed signal, a 1-d array.   
   
   N=y.shape[0]
   Fa=symFmatrix(fb)
   #invert Fa matrix for synthesis after removing last dim:
   Fs=np.linalg.inv(Fa[:,:,0])
   #add again last dimension for function polmatmult:
   Fs=np.expand_dims(Fs, axis=-1)
   Dinv=Dinvmatrix(N)

   #add first dimension to y for polmatmult:
   y=np.expand_dims(y,axis=0)
   xp=DCT4(y)
   xp=polmatmult(xp,Dinv)
   xp=polmatmult(xp,Fs)
   xr=polyphase2x(xp)
   return xr


#Testing:
if __name__ == '__main__':
   import numpy as np
   import matplotlib.pyplot as plt

   #Number of subbands:
   N=4
   D=Dmatrix(N)
   Dinv=Dinvmatrix(N)
   #Filter bank coefficients for sine window:
   #fb=np.sin(np.pi/(2*N)*(np.arange(int(1.5*N))+0.5))
   fb=np.loadtxt("MDCTcoeff.txt") #Coeff. from optimization
   print("fb=", fb)
   #input test signal, ramp:
   x=np.arange(64)
   plt.plot(x)
   plt.title('Input Signal')
   plt.xlabel('Sample')
   plt.show()
   y=MDCTanafb(x,N,fb); print("y=\n", y)
   plt.imshow(np.abs(y))
   plt.title('MDCT Subbands')
   plt.xlabel('Block No.')
   plt.ylabel('Subband No.')
   plt.show()
   xr=MDCTsynfb(y,fb)
   plt.plot(xr)
   plt.title('Reconstructed Signal')
   plt.xlabel('Sample')
   plt.show()
   y=np.zeros((4,16))
   y[0,0]=1
   xr=MDCTsynfb(y,fb)
   plt.plot(xr[0:3*N])
   plt.title('Impulse Response of Modulated Synthesis Subband 0')
   plt.xlabel('Sample')
   plt.show()