import numpy as np
import matplotlib.pyplot as plt

def fun01(x: float):
    return x**3 - 7*(x**2) + 28

def fun02(x: float):
    return (9 - x**2)**0.5

def fun03(x: float):
    return np.sin(100 * x)

def fun04(x: float):
    return np.cos(x) + (1/200)*np.sin(200*x)


def fun05(x: float):
    return np.power(x, 1/3)

def fun06(x: np.ndarray):
    return (x / np.abs(x)) * np.power(np.abs(x), 1/3)

# x = np.arange(-3, 3, 0.001)
# y = fun01(x)
# y = fun02(x)
# x = np.arange(-0.1, 0.1, 0.001)
# y = fun03(x)

# x = np.arange(-4, 4, 0.001)
# x = np.arange(-1, 1, 0.001)
# x = np.arange(-0.2, 0.2, 0.001)
# y = fun04(x)

x = np.arange(-5, 5, 0.01)
# y = fun05(x)
y = fun06(x)

# plt.plot(x, y, "r--", x, x, "b", x, -x+3*(2**0.5), "y")
plt.plot(x, y)

# add this to make the scales on both axes equal
# plt.axis('square')
# plt.axis('equal')

# plt.title("fun01")
plt.xlabel("x")
plt.ylabel("y")
plt.show()