import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('om495t4.jpg')
print(img)
img_tinted = img*[1, 0.9, 0.1]
img_tinted = imresize(img_tinted, (100,50))
plt.subplot(2,1,1)
plt.imshow(img)
plt.subplot(2,1,2)
plt.imshow(np.uint8(img_tinted))
plt.show()