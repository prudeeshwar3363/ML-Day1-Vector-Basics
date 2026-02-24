import numpy as np

def dot_product(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

a = np.array([45, 44, 33, 55, 84])
b = np.array([48, 39, 26, 78, 12])

print(dot_product(a, b))