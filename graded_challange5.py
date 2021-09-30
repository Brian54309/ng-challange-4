import numpy as np
import sympy


tensor_a = np.array([[[23,50],[7,12]],[[57,67],[99,43]],[[75,21],[57,12]],[[87,26],[18,84]]])
#print(tensor_a)

a = np.array([[23,50,19],[7,12,109],[57,67,98]])
b=np.array([[17],[22],[19]])

print(np.dot(a,b))

print(a.T)
a_inv = np.linalg.inv(a)
print(a_inv)