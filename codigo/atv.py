from matplotlib import pyplot as plt
import numpy as np
import cv2


obj_img = cv2.imread("img\tia1.png")
obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)


imgOpenCV = cv2.imread("img\tia1.png")
largura, altura, canais = imgOpenCV.shape


def rescaleImage(img, escala):

    alturam = int((altura*escala)/100)
    larguram = int((largura*escala)/100)
    taman = (alturam, larguram)
    rescaleImage = cv2.resize(obj_img, taman)
    print(obj_img.shape)
    print(rescaleImage.shape)
    plt.imshow(obj_img)
    plt.show()
    cv2.waitKey(0)
    plt.imshow(rescaleImage)
    plt.show()
    cv2.waitKey(0)


rescaleImage(obj_img, 60)

# for y in range(0, altura):
#     for x in range(0, largura):
#         azul = imgOpenCV.item(y, x, 0)
#         verde = imgOpenCV.item(y, x, 1)
#         vermelho = imgOpenCV.item(y, x, 2)

#         imgOpenCV.itemSet
#print(x, y, ":", verde, vermelho, azul)
