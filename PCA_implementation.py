#!/usr/bin/env python
# coding: utf-8


import cv2
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

DIR = 'MalariaDrugImagesGHS'
DIM = 128

count = len(os.listdir(DIR))
images = np.zeros([count, DIM, DIM], dtype='uint8')

# Read and resize images
scaler = StandardScaler()
for (i,image) in zip(range(len(os.listdir(DIR)[:])), os.listdir('MalariaDrugImagesGHS')[:]):
    im_arr = cv2.imread(os.path.join(DIR, image))
    im_arr = cv2.cvtColor(im_arr, cv2.COLOR_BGR2GRAY)
    im_arr = cv2.resize(im_arr, (DIM, DIM))
    im_arr = scaler.fit_transform(im_arr)
    plt.imshow(im_arr)
    images[i] = im_arr

images = images.reshape(count, -1)

'''
pca = PCA(n_components=200)
pca.fit(images)

'''
# pca = PCA(.99)
# lower_dimensional_data = pca.fit_transform(images)
# pca.n_components_


# In[89]:


for var in [0.99, 0.9, 0.85, 0.8, 0.75, 0.3]:
    pca = PCA(var)
    pca.fit(images)
    lower_dimensional_data = pca.fit_transform(images)
    approximation = pca.inverse_transform(lower_dimensional_data)
    plt.figure(figsize=(8,4));

    # Original Image
    plt.subplot(1, 2, 1);
    plt.imshow(images[1].reshape(DIM,DIM),
                  cmap = plt.cm.gray, interpolation='nearest',
                  clim=(0, 255));
    plt.xlabel(str(images[0].shape[0]) + ' components', fontsize = 14)
    plt.title('Original Image', fontsize = 20);

    # 154 principal components
    plt.subplot(1, 2, 2);
    plt.imshow(approximation[1].reshape(DIM, DIM),
                  cmap = plt.cm.gray, interpolation='nearest',
                  clim=(0, 255));
    plt.xlabel(str(pca.n_components_) + ' components', fontsize = 14)
    plt.title(str(var*100) + '% of Explained Variance', fontsize = 20);
    plt.show()
    print('Keeping ' +str(var*100) +' percent of the original data requires: ' + str(pca.n_components_) + ' bytes')

