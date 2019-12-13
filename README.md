# Qiskit-Hackathon

Title: Quantum image dataset loading

Description:
This project converts given image dataset to quantum processable data(qubits) by utilizing PCA for dimensionality reduction and initial states for generating qubits. It can analyze the number of PCA components and produce the transformed qubits of an image dataset for a chosen IBM quantum device or simulator. The variance percentage that is being kept by PCA is also given as feedback to the user.

Requirements:
* Python (3.6 and above) 

Installation of python library dependencies
>> pip install -r requirements.txt

Usage Of Code: 
Call the resize_image function to parse in the folder directory of the image dataset and the n by n pixels to down size the images. 
>> image = resize_image(Directory, no. of pixel)		# n by n pixel dimension

Use the pca function to parse in the images and the required no. of components
>> pca(images, no. of components) 
