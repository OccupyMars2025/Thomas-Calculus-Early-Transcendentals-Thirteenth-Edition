def fun01(x: float):
    return x**3 - 7*(x**2) + 28

def fun02(x: float):
    return (9 - x**2)**0.5


import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3, 3, 0.01)
# y = fun01(x)
y = fun02(x)
plt.plot(x, y, "r--", x, x, "b", x, -x+3*(2**0.5), "y")

# add this to make the scales on both axes equal
plt.axis('square')

# plt.title("fun01")
plt.xlabel("x")
plt.ylabel("y")
plt.show()