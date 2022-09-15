from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
img = np.zeros((300, 600, 3), dtype=np.uint8)

cv.rectangle(img, (0, 0), (200, 300), (255, 0, 0), -1)
cv.rectangle(img, (200, 0), (400, 300), (0, 255, 0), -1)
cv.rectangle(img, (400, 0), (600, 300), (0, 0, 255), -1)
cv.imshow("atvd", img)
cv.waitKey(0)
cv.destroyAllWindows()
