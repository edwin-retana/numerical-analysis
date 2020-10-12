#%%


import matplotlib.pyplot as plt
import numpy as np
import time
from PIL import Image

#%%
#convert image to black and white (with color is more complicated in python)
img = Image.open('/Users/yandthj/Downloads/img_54.jpg')
imggray = img.convert('LA')
plt.figure(figsize=(9,6))
plt.imshow(imggray);

#%%
#convert image data into numpy matrix, plot result to show no change
imgmat=np.array(list(imggray.getdata(band=0)),float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.matrix(imgmat)
plt.figure(figsize=(9,6))
plt.imshow(imgmat, cmap='gray');
#%%
U, sigma, V = np.linalg.svd(imgmat)
reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
plt.imshow(reconstimg, cmap='gray');
# %%
for i in range(5, 51, 5):
    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()
# %%
