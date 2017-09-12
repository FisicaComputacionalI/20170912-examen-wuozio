import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 4.5 * np.sin(np.pi*t)+2013

t1 = np.arange(0.0,5.0,0.1)

plt.plot(t1, f(t1), 'bo')
plt.savefig('prob2.png')
plt.show()
