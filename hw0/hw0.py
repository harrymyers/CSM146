import numpy as np
import matplotlib.pyplot as plt

# problem 10

#(a) 
mean = [0, 0]
cov = [[1, 0],
       [0, 1]]
samples = np.random.multivariate_normal(mean, cov, 1000) # 1000 gaussian dist 

# x = [x1, x2] make a scatter plot xq vs x2
plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)
plt.title("Standard Gaussian (mean = [0,0], identity covariance)")
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig("problem10a.png", dpi=300)
plt.close()
# Circular cloud centered at (0,0)
# No direction preference

#(b) Change mean to (-1, 1)
mean = [-1, 1]
samples = np.random.multivariate_normal(mean, cov, 1000)

plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)
plt.title("Shifted Mean (-1, 1)")
plt.savefig("problem10b.png", dpi=300)
plt.close()
# Same shape as (a)
# Entire cloud shifts to (-1, 1)

#(c) Double the variance
mean = [0, 0]
cov = [[2, 0],
       [0, 2]]

samples = np.random.multivariate_normal(mean, cov, 1000)

plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)
plt.title("Increased Variance")
plt.savefig("problem10c.png", dpi=300)
plt.close()
# Still circular
# More spread out (wider cloud)

#(d) Positive covariance (0.5)
cov = [[1, 0.5],
       [0.5, 1]]

samples = np.random.multivariate_normal([0, 0], cov, 1000)

plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)
plt.title("Positive Correlation (0.5)")
plt.savefig("problem10d.png", dpi=300)
plt.close()
# Ellipse tilted upward
# Points increase together (↗ direction)

#(e) Negative covariance (-0.5)
cov = [[1, -0.5],
       [-0.5, 1]]

samples = np.random.multivariate_normal([0, 0], cov, 1000)

plt.scatter(samples[:, 0], samples[:, 1], alpha=0.5)
plt.title("Negative Correlation (-0.5)")
plt.savefig("problem10e.png", dpi=300)
plt.close()
# Ellipse tilted downward
# One increases while the other decreases (↘ direction)


# # Problem 11
# # Write a Python program to compute the eigenvector 
# # corresponding to the largest eigenvalue of
# # the following matrix and submit the computed eigenvector

# A = np.array([[1, 0],
#               [1, 3]])

# # Compute eigenvalues and eigenvectors
# eigenvalues, eigenvectors = np.linalg.eig(A)

# # Find index of largest eigenvalue
# max_index = np.argmax(eigenvalues) # max index 0

# # Get corresponding eigenvector
# largest_eigenvector = eigenvectors[:, max_index]

# # Print results
# print("Eigenvalues:", eigenvalues)
# print("Eigenvectors:\n", eigenvectors)
# print("Largest Eigenvalue:", eigenvalues[max_index])
# print("Eigenvector corresponding to largest eigenvalue:")
# print(largest_eigenvector)