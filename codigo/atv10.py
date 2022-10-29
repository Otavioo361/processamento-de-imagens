import cv2
import numpy as np


def showImage(img):
    img= cv2.imread("img/otavio.jpeg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("original",img)
    

def main():

    min = np.array([2, 58, 100], dtype = "uint8")
    max = np.array([253, 228, 235], dtype = "uint8")

    image = cv2.imread("img/otavio.jpeg")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    imageCo = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    skinRegionHSV = cv2.inRange(imageCo, min, max)
    skin = cv2.bitwise_and(image, image, mask = skinRegionHSV)

    """
    A função numpy.hstack() é usada para empilhar a sequência de arrays de entrada
    horizontalmente (ou seja, coluna sábia) para fazer um único array.
    """
    cv2.imwrite("mascara.png", np.hstack([image, skin]))
    showImage(skinRegionHSV)

if __name__ == "__main__":
    main()