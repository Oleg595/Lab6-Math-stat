import numpy as np
import math
import matplotlib.pyplot as plt

def average(x, n):
    result = 0.
    for i in range(n):
        result += x[i]
    result /= n
    return result

def quad_average(x, n):
    result = 0.
    for i in range(n):
        result += x[i] * x[i]
    result /= n
    return result

def mediana(x, size):
    if size % 2 == 1:
        num = (size - 1) / 2 + 1
        result = x.index(num)
    else:
        num = math.ceil(size / 2)
        result = (x[num] + x[num + 1]) / 2.
    return result

def mnk_B(x, y):
    result = np.zeros(2)
    z = np.zeros(20)
    for i in range(20):
        z[i] = x[i] * y[i]
    n1 = average(x, 20)
    n2 = average(y, 20)
    result[1] = (average(z, 20) - n1 * n2) / (quad_average(x, 20) - (n1 * n1))
    result[0] = n2 - result[1] * n1
    return result

def Rq(x, y):
    result = 0.
    med_x = mediana(x, 20)
    med_y = mediana(y, 20)
    for i in range(20):
        result += np.sign(x[i] - med_x) * np.sign(y[i] - med_y)
    result /= 20
    return result

def quartile(x, size):
    p = .25
    num1 = math.floor(size * p + 1)
    num2 = math.floor(size * (1 - p) + 1)
    return (x[num1] + x[num2]) / 2

def mnm_B(x, y):
    r_q = Rq(x, y)
    list(y).sort()
    list(x).sort()
    k_q = quartile(y, 20) / quad_average(y, 20)
    l = 5
    j = 16
    qy = (y[j] - y[l]) / k_q
    qx = (x[j] - x[l]) / k_q
    result = np.zeros(2)
    result[1] = r_q * qy / qx
    result[0] = mediana(y, 20) - result[1] * mediana(x, 20)
    return result


x = np.zeros(20)
e = np.random.normal(0, 1, 20)
a = -1.8
for i in range(20):
    x[i] = a + 0.2 * i
y = np.zeros(20)
y += 2 * x + 2
plt.plot(x, y, label= "Модель")
y = np.zeros(20)
y += 2 * x + 2 + e
plt.scatter(x, y, label= "Выборка")
B = mnk_B(x, y)
y = B[0] + B[1] * x
plt.plot(x, y, label= "МНК")
print(B[0], B[1])
y = np.zeros(20)
y += 2 * x + 2 + e
B1 = mnm_B(x, y)
y = B1[0] + B1[1] * x
plt.plot(x, y, label= "МНМ")
print(B1[0], B1[1])
plt.title("Без возмущений")
plt.legend()
plt.show()

y = np.zeros(20)
y += 2 * x + 2
plt.plot(x, y, label= "Модель")
y = np.zeros(20)
y += 2 * x + 2 + e
y[19] -= 10
y[0] += 10
plt.scatter(x, y, label= "Выборка")
B = mnk_B(x, y)
y = B[0] + B[1] * x
plt.plot(x, y, label= "МНК")
print(B[0], B[1])
y += 2 * x + 2 + e
y[19] -= 10
y[0] += 10
B1 = mnm_B(x, y)
y = B1[0] + B1[1] * x
plt.plot(x, y, label= "МНМ")
print(B1[0], B1[1])
plt.title("С возмущениями")
plt.legend()
plt.show()
