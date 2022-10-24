
import numpy as np
import cv2
from matplotlib import pyplot as plt

normal = cv2.imread("img\\img.png")
verde = cv2.imread("img\\img1.png")
alturaNormal, larguraNormal, _ = normal.shape
verde = cv2.resize(verde, (larguraNormal, alturaNormal))
# fazendo a soma, a função  pega a foto e o proximo e a sua intensidade, no caso vai multiplicar por 0.5
montage = cv2.addWeighted(normal, 0.5, verde, 0.25, 0)

cv2.imshow("montage", montage)
cv2.waitKey(0)
cv2.destroyAllWindows()
