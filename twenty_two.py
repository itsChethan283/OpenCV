import cv2 
import numpy as np
from matplotlib import pyplot as plt

imgqw = cv2.imread("road.jpg")
img = cv2.cvtColor(imgqw, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()