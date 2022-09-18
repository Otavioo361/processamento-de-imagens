from matplotlib import pyplot as plt
import numpy as np
import cv2
obj_img = cv2.imread("img\\bola.jpg")
bolas = obj_img[287:287 + 50, 336:336 + 60]
#obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)


def paste(obj_img, bolas):
    obj_img[217: 217 + bolas.shape[0], 110: 110 + bolas.shape[1]] = bolas
    cv2.imshow("atvd", obj_img)
    #plt.imshow("atvdnew", newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


paste(obj_img, bolas)
