import numpy as np
a = np.array([45, 44, 33, 55, 84])
b = np.array([48, 39, 26, 78, 12])

print("Vector A: ", a)
print("Vector B: ", b)

# vector operations
add = a+b
sub = a-b
multi = a*b
dot_prod = np.dot(a, b)

print("Addition of A, B: ", add)
print("Subtraction of A, B: ", sub)
print("Multiplication of A, B: ", multi)
print("Dot Product of A, B: ", dot_prod)