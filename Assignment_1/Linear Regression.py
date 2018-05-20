import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math as mat

# dataset
year = np.arange(1899, 1923, 1)
m = len(year)
p = np.log([100, 101, 112, 122, 124, 122, 143, 152, 151, 126, 155, 159, 153, 177, 184, 169, 189, 225, 227, 223, 218, 231, 179, 240])
L = np.log([100, 105, 110, 117, 122, 121, 125, 134, 140, 123, 143, 147, 148, 155, 156, 152, 156, 183, 198, 201, 196, 194, 146, 161])
K = np.log([100, 107, 114, 122, 131, 138, 149, 163, 176, 185, 198, 208, 216, 226, 236, 244, 266, 298, 335, 366, 387, 407, 417, 431])

# processing data
X = np.insert(np.array([L, K]).T, 0, 1, axis=1)
y = np.array(p).T

# a = 1
# params = np.array([1, a, a - 1]) # beta and alpha
# ln(p) = ln(beta) + alpha*ln(L) + (1-alpha)*ln(K)
# find the root
params = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
print(params)
def hypothesis(params):
    return np.dot(X, params.T)
cost_function = sum((hypothesis(params) - y)**2)/(2*m)
print("The cost is: %f" % cost_function)

# plot it
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(L, K, p, c='r', marker='o')
ax.set_xlabel("L")
ax.set_ylabel("K")
ax.set_zlabel("p")
ax.plot(L, K, hypothesis(params), c='b')
plt.show()

def predict(data):
    process_data = np.insert(np.log(data), 0, 1, axis=0)
    return mat.e**np.dot(process_data, params.T)

predict_data = np.array([[143, 198], [170, 450], [174, 250], [180, 316]])
for p in predict_data:
    print("Predict for L = %d, K = %d: %f" % (p[0], p[1], predict(p)))