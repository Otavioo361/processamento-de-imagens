from matplotlib import pyplot as plt
import numpy as np
import cv2
obj_img = cv2.imread("bola.jpg")
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
bola = obj_img[287:287+50, 336:336+60]
plt.imshow(bola)
cv2.waitKey(0)
cv2.destroyAllWindows()
