
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Transforma BGR em RGB


def showImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def tiraMedia(largura, altura, c1, c2, c3):
    # Usando a função np.sum() que soma todos os elementos da matriz
    a = c1.sum()
    b = c2.sum()
    c = c3.sum()

    # Pegando o número total de pixels
    numPixels = largura * altura
    a = a // numPixels
    b = b // numPixels
    c = c // numPixels

    print("Média de azul por pixel     = ", a)
    print("Média de verde por pixel    = ", b)
    print("Média de vermelho por pixel = ", c)

    if (a > (b and c)):
        print("\nA imagem é mais AZUL!")
    if (b > (a and c)):
        print("\nA imagem é mais VERDE!")
    if (c > (a and b)):
        print("\nA imagem é mais VERMELHA")


def main():

    imagem = cv2.imread("img\\mustang.png")
    altura, largura, canaisDeCor = imagem.shape

    # Dividindo cada canal de cor em um vetor
    # Splitusado para dividir a imagem colorida/multicanal em imagens de canal único separadas
    b, g, r = cv2.split(imagem)

    tiraMedia(largura, altura, b, g, r)

    cv2.imshow("Imagem azul", b)  # azul
    cv2.imshow("Imagem verde", g)  # verde
    cv2.imshow("Imagem vermelha", r)  # vermelho

    cv2.waitKey(0)


if __name__ == "__main__":
    main()


# from matplotlib import pyplot as plt
# import numpy as np
# import cv2
# obj_img = cv2.imread("img\\mustang.png")


# def createVermelho(obj_img):
#     vermelho = obj_img[:, :, 2]
#     imgVermelho = np.zeros(obj_img.shape, np.uint8)
#     imgVermelho[:, :, 2] = vermelho
#     cv2.imwrite("img//imgVermelha.png", imgVermelho)
#     cv2.imshow("atvdVermelha", imgVermelho)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# def createVerde(obj_img):
#     verde = obj_img[:, :, 1]
#     ImgVerde = np.zeros(obj_img.shape, np.uint8)
#     ImgVerde[:, :, 1] = verde
#     cv2.imwrite("img//imgVerde.png", ImgVerde)
#     cv2.imshow("atvdVerde", ImgVerde)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# def createAzul(obj_img):
#     azul = obj_img[:, :, 0]
#     ImgAzul = np.zeros(obj_img.shape, np.uint8)
#     ImgAzul[:, :, 0] = azul
#     cv2.imwrite("img//imgAzul.png", ImgAzul)
#     cv2.imshow("atvdAzul", ImgAzul)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


# def commonColor(obj_img):
#     createAzul(obj_img)
#     createVerde(obj_img)
#     createVermelho(obj_img)
#     vermei, Verdi, zul = 0, 0, 0

#     altura, largura, canais = obj_img.shape

#     for y in range(altura):
#         for x in range(largura):
#             vermei += obj_img.item(y, x, 2)
#             Verdi += obj_img.item(y, x, 1)
#             zul += obj_img.item(y, x, 0)
#     vermei = vermei/(altura*largura)
#     Verdi = Verdi/(altura*largura)
#     zul = zul/(altura*largura)

#     if vermei > Verdi and vermei > zul:
#         print("vermei")
#     elif Verdi > vermei and Verdi > zul:
#         print("Verdi")
#     elif zul > vermei and zul > Verdi:
#         print("zul")


# createVermelho(obj_img)
# createVerde(obj_img)
# createAzul(obj_img)
# commonColor(obj_img)
