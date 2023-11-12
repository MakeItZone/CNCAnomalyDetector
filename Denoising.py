# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# %%

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams.update({'font.size': 18})
#create sample signal with 2 frequencies
dt=0.001
t=np.arange(0,1,dt)
f=np.sin(2*np.pi*50*t)+np.sin(2*np.pi*120*t)  #sum of 2 frequencies
f_clean = f
f=f+2.5*np.random.randn(len(t))               #Add some noise
plt.plot(t,f,color='pink', label='Noisy')
plt.plot(t,f_clean,color='blue', label='Clean')
plt.xlim(t[0],t[-1])
plt.xlabel('radians')
plt.ylabel('amplitude')
plt.legend()
# -

#compute the FFT algo
n = len(t)
fhat = np.fft.fft(f,n)                     #compute the FFT
PSD = fhat * np.conj(fhat)/n               #power spectrum 
freq = (1/(dt*n)) * np.arange(n)           #x-axis of frequencies 
L = np.arange(1,np.floor(n/2),dtype='int') #only plot 1st half
plt.plot(freq[L], PSD[L],color='red', label='Noisy')
plt.xlim(freq[L[0]],freq[L[-1]])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density')
plt.legend()
plt.show()


#Use PSD to filter out noise
indices = PSD > 100        # Find all freqs with large power
PSDclean = PSD * indices   # zero out all others via kronecker delta
fhat = indices*fhat        # zero out small fourier coffef. in Y
ffilt = np.fft.ifft(fhat)  # inverse fFFT for filtered time signal
#plot
fig,axs = plt.subplots(2,1)
plt.sca(axs[0])
plt.plot(t,f,color='pink', label='Noisy')
plt.plot(t,f_clean,color='blue',  label='Clean')
plt.xlim(t[0],t[-1])
plt.xlabel('Radians')
plt.ylabel('Amplitude')
plt.legend()
plt.sca(axs[1])
plt.plot(t, ffilt,color='blue', label='Filtered')
plt.xlim(t[0],t[-1])
plt.xlabel('Radians')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()


