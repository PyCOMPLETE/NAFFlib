import sys
sys.path.append('..')
sys.path.append('.')
import nafflib as NAFF

import numpy as np

np.random.seed(123456)
N=100
noise_rms=0.1
i = np.linspace(1,N,N)

q_true=6.24783351

x=np.empty_like(i,dtype=np.complex128)
print '                  True     frequency is Q_true = %1.10f'%q_true

x  = 1*np.cos(2*np.pi*q_true*i) + 0j*np.sin(2*np.pi*q_true*i)
print '(real           ) Estimated frequency is Q_hat = %1.10f'%NAFF.get_tune(x)

x  = 1*np.cos(2*np.pi*q_true*i) + 1j*np.sin(2*np.pi*q_true*i)
print '(complex        ) Estimated frequency is Q_hat = %1.10f'%NAFF.get_tune(x)

x  = 1*np.cos(2*np.pi*q_true*i) + np.random.normal(0,noise_rms,N) +0j*np.sin(2*np.pi*q_true*i)
print '(real    + noise) Estimated frequency is Q_hat = %1.10f'%NAFF.get_tune(x)

x  = 1*np.cos(2*np.pi*q_true*i) + np.random.normal(0,noise_rms,N) +1j*np.sin(2*np.pi*q_true*i) + 1j*np.random.normal(0,noise_rms,N)
print '(complex + noise) Estimated frequency is Q_hat = %1.10f'%NAFF.get_tune(x)
