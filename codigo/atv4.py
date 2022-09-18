from matplotlib import pyplot as plt
import numpy as np
import cv2


def triagulo(t1, t2, t3):
    obj_img = cv2.imread("img\\mini couper.png")
    cv2.line(obj_img, t1, t2, (0, 0,  0), 1)
    cv2.line(obj_img, t2, t3, (0, 0,  0), 1)
    cv2.line(obj_img, t3, t1, (0, 0, 0), 1)
    trianguloC = np.array([t1, t2, t3])
    cv2.drawContours(obj_img, [trianguloC], 0, (0, 0, 0), -1)
    cv2.imwrite("img\\minitriang.png", obj_img)
    cv2.imshow("atvd", obj_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


triagulo((556, 518), (491, 569), (518, 645))
