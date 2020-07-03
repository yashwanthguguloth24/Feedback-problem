from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import numpy as np

w0=np.logspace(-1,9,10**5)

gain = [((2*np.pi)**2)*(10**16)]
poles=[-2*np.pi*(10**6),-2*np.pi*(10**7)]
zeros=[]
system = signal.lti(zeros,poles,gain)
w , mag, phase = signal.bode(system,w0)

T1=159.15*(10**-6)
system1=signal.lti([T1,1],[1])
w1,mag1,phase1=signal.bode(system1,w0)

T2=5000*(10**-6)
system2=signal.lti([T2,1],[1])
w2,mag2,phase2=signal.bode(system2,w0)

T3=5*(10**-6)
system3=signal.lti([T3,1],[1])
w3,mag3,phase3=signal.bode(system3,w0)



plt.semilogx(w0, mag,label='plot of G')
plt.semilogx(w0, mag1,label='$\u03C4 =\u03C4_{min}=159.15\mu s$')
plt.semilogx(w0, mag2,label='$\u03C4=5000\mu s >\u03C4_{min}$')
plt.semilogx(w0, mag3,label='$\u03C4=5\mu s <\u03C4_{min}$')
plt.ylabel('Mag(dB)')
plt.xlabel('frequency(rad/s)')
plt.title('Plot of G and 1/H in dB')
plt.grid()
plt.legend()
plt.show()

