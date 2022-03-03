import numpy as np
import matplotlib.pyplot as plot


def f(x):
    return x**3 - 9*x**2 + 22*x - 15

interval = np.linspace(1, 6)
plot.plot(interval, f(interval))
plot.grid()
plot.show()