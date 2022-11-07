import cv2
import numpy as np


def showImage(img):
    cv2.imshow("original",img)
    cv2.waitKey(0)
    

def main():
    img= cv2.imread("img/otavio.jpeg")
    showImage(img)
    min = np.array([2, 58, 100], dtype = "uint8")
    max = np.array([253, 228, 235], dtype = "uint8")

    image = cv2.imread("img/otavio.jpeg")
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    imageCo = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #função inrange vai fazer a comparação entre as matrizes,caso nao estiver ele zera o
    shinRegion = cv2.inRange(imageCo, min, max)
    skin = cv2.bitwise_and(image, image, mask = shinRegion)

    """
    A função numpy.hstack() é usada para empilhar a sequência de arrays de entrada
    horizontalmente (ou seja, coluna sábia) para fazer um único array,mesclando a imagem  com a skin.
    """
    cv2.imwrite("mascara.png", np.hstack([image, skin]))
    showImage(shinRegion)

if __name__ == "__main__":
    main()

#fim da atividade da tarefa4