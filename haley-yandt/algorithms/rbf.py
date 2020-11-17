#%%
import numpy as np
import math
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from numpy.linalg import pinv
from numpy.linalg import norm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#%%
#transfer function
def rbf1(A):
    A = np.power(A, 3)
    return A
# %%
#First define the data
X = np.random.normal(size = (1500, 2))
#get Y data
#first column squared
column1 = np.power(X[:,0], 2)
column2 = np.power(X[:,1], 2)
powerSum = np.add(column1, column2)
element_divide = powerSum / 4
#noise
noise = 0.15 * (np.random.normal(size = (1500, 1)))
element_divide = np.reshape(element_divide, (1500, 1))
Y = element_divide + noise
#print(Y.shape)
# %%
#split into training and test, (300 points for training)
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.8)
print(Xtrain.shape)
print(Ytrain.shape)
print(Xtest.shape)
print(Ytest.shape)
#%%
#create the radial basis function
#use 10 points chosen at random from the data set as our set of centers
temp = np.random.permutation(1500)
Centers = X[temp[0:10], :]
print(Centers.shape)
A = distance.cdist(Xtrain, Centers, 'euclidean')
#converts to square form 
#A = distance.squareform(A)
print(A.shape)
#transfer function is cubic
Phi = rbf1(A)
#get weights using pseudo-inverse of phi
alpha = np.matmul((pinv(Phi)),Ytrain)
# %%
#compute the new edm
A = distance.cdist(Xtest, Centers, 'euclidean')
Phi = rbf1(A)
Yout = np.matmul(Phi, alpha)
m, n = Ytest.shape
print(m, n)
#%%
Err = []
#the error is the norm of the difference
for j in range(m):
    Err.append(norm(Ytest[j,:]-Yout[j,:]))
# %%
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(Xtest[:,0], Xtest[:,1], Yout, marker='.')
plt.show()
# %%
num_bins = 10
n, bins, patches = plt.hist(Err, num_bins, facecolor='blue', alpha=0.5)
plt.show()
# %%
