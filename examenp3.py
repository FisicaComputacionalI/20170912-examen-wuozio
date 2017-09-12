import numpy as np
import matplotlib.pyplot as plt

def f(a):
    return a + 1995
def x(y):
    return 4.5 * np.sin(np.pi*y)+2013
a1 = np.arange(0,22,0.1)
y1 = np.arange(0.0,22,0.1)
plt.figure(1)
plt.subplot(211)
plt.plot(a1,f(y1), 'D',y1,x(y1),'b')
plt.subplot(212)
plt.plot(y1, x(y1))
plt.savefig('prob3.png')
plt.show()
