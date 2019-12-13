import cv2
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


DIM = 128

def resize_images(dir_, size=DIM):
    count = len(os.listdir(dir_))
    images = np.zeros([count, size, size], dtype='uint8')

    # Read and resize images
    scaler = StandardScaler()
    for (i,image) in zip(range(len(os.listdir(dir_))), os.listdir(dir_)):
        im_arr = cv2.imread(os.path.join(dir_, image))
        im_arr = cv2.cvtColor(im_arr, cv2.COLOR_BGR2GRAY)
        im_arr = cv2.resize(im_arr, (size, size))
        im_arr = scaler.fit_transform(im_arr)
        images[i] = im_arr
    images = images.reshape(count, -1)
    return images

def pca(images, components):
    pca = PCA(n_components= components)
    pca.fit(images)
    lower_dimensional_data = pca.fit_transform(images)
    expected_variance = pca.explained_variance_ratio_.cumsum()[-1]
    return (lower_dimensional_data, expected_variance)
