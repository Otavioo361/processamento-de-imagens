from matplotlib import pyplot as plt
import numpy as np
import cv2
obj_img = cv2.imread("img\\mustang.png")


def createVermelho(obj_img):
    vermelho = obj_img[:, :, 2]
    imgVermelho = np.zeros(obj_img.shape, np.uint8)
    imgVermelho[:, :, 2] = vermelho
    cv2.imwrite("img//imgVermelha.png", imgVermelho)
    cv2.imshow("atvdVermelha", imgVermelho)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def createVerde(obj_img):
    verde = obj_img[:, :, 1]
    ImgVerde = np.zeros(obj_img.shape, np.uint8)
    ImgVerde[:, :, 1] = verde
    cv2.imwrite("img//imgVerde.png", ImgVerde)
    cv2.imshow("atvdVerde", ImgVerde)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def createAzul(obj_img):
    azul = obj_img[:, :, 0]
    ImgAzul = np.zeros(obj_img.shape, np.uint8)
    ImgAzul[:, :, 0] = azul
    cv2.imwrite("img//imgAzul.png", ImgAzul)
    cv2.imshow("atvdAzul", ImgAzul)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def commonColor(obj_img):
    createAzul(obj_img)
    createVerde(obj_img)
    createVermelho(obj_img)
    vermei, Verdi, zul = 0, 0, 0

    altura, largura, canais = obj_img.shape

    for y in range(altura):
        for x in range(largura):
            vermei += obj_img.item(y, x, 2)
            Verdi += obj_img.item(y, x, 1)
            zul += obj_img.item(y, x, 0)
    vermei = vermei/(altura*largura)
    Verdi = Verdi/(altura*largura)
    zul = zul/(altura*largura)

    if vermei > Verdi and vermei > zul:
        print("vermei")
    elif Verdi > vermei and Verdi > zul:
        print("Verdi")
    elif zul > vermei and zul > Verdi:
        print("zul")


createVermelho(obj_img)
createVerde(obj_img)
createAzul(obj_img)
commonColor(obj_img)
