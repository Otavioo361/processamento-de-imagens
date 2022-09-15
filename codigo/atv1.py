from matplotlib import pyplot as plt
import numpy as np
import cv2

cap = cv2.VideoCapture("img\\video.mp4")
obj_img = cv2.imread("img\\lambo.png")

if (cap.isOpened() == False):
    print("Arquivo de video nao aberto")

    if (obj_img.isOpened() == False):
        print("Arquivo de foto nao aberto ")


while (cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('Frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            plt.imshow(obj_img)
            plt.show()
            break

    else:
        break

cap.release()

cv2.destroyAllWindows()
