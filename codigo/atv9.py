import numpy as np
import cv2
#from matplotlib import pyplot as plt

def showImage(img):    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img)
    # plt.show()

#Redimensiona uma imagem
def resizeImage(image, scalePercent):
    width = int(image.shape[1] * scalePercent / 100)
    height = int(image.shape[0] * scalePercent / 100)
    image = cv2.resize(image, (width, height))

    return image

#Faz a sobreposição de duas imagens 
def addImageOverlay(background, foreground, transLar, transAl):

    #Pegando a altura e a largura da imagem da frente e da de trás
    atrasAl, atrasLa, _ = background.shape
    frenteAl, frenteLar, _ = foreground.shape

    #Subtraindo altura e largura da imagem, e pegando "oque sobra"
    remainingH, remainingW = atrasAl - frenteAl, atrasLa - frenteLar


    #Parte do cenário do fundo em que a imagem será adicionada
    #photoshop mode
    crop = background[transAl : frenteAl + transAl, transLar : frenteLar + transLar]

    #Transformamos o foreground em imagem com tons de cinza e criamos uma máscara binária da mesma com a binarização (cv2.threshold)
    foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY) #Separa os pixels que compoem a imagem do fundo
    ret, maskFore = cv2.threshold(foregroundGray, 210, 255, cv2.THRESH_BINARY)  #Linearização

    #Agora aplicamos uma operação de AND binário na imagem recortada 'crop'. No caso, realizar a operação binária entre a mesma imagem não terá efeito. Só que, com a inclusão da máscara no terceiro parâmetro, os pixels pretos de maskFore serão ignorados e, portanto, ficarão escuros. Com isso temos a marcação em que vamos incluir o foreground posteriormente.
    backWithMask = cv2.bitwise_and(crop, crop, mask = maskFore)
    foreWithMask = cv2.bitwise_not(maskFore)
    foreWithMask = cv2.bitwise_and(foreground, foreground, mask = foreWithMask)

    #Faremos a composição entre 'frente' e 'fundo', compondo o foreground na imagem extraída do background.
    combinedImage = cv2.add(foreWithMask, backWithMask)

    #Adicionamos a imagem gerada no background final.
    copyImage = background.copy()
    copyImage[transLar:frenteAl + transLar, transAl:frenteLar + transAl] = combinedImage

    return copyImage

#Passa duas imagens, e o efeito de transparência
def addBlendingEffect(firstImage, secondImage, weight):

    #Carregando as duas imagens
    firstImageGray = cv2.cvtColor(firstImage, cv2.COLOR_BGR2GRAY) #Transformando para tons de cinza
    secondImageGray = cv2.cvtColor(secondImage, cv2.COLOR_BGR2GRAY)

    mask = firstImageGray - secondImageGray  #Imagem "negativa", subtração de matrizes
    ret, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY) #Linearização

    #Cópia da primeira imagem
    copyImg = firstImage.copy()

    altura, largura, = mask.shape

    #Percorrendo toda a imagem
    for y in range(0, altura):
        for x in range(0, largura):

            #Se na posição da máscara o pixel for branco
            if mask.item(y, x) == 255:

                #Soma ponderada entre 2 pixels da mesma posição
                blendingPixelBlue = firstImage.item(y, x, 0) * (1.0 - weight) + secondImage.item(y, x, 0) * weight
                blendingPixelGreen = firstImage.item(y, x, 1) * (1.0 - weight) + secondImage.item(y, x, 1) * weight
                blendingPixelRed = firstImage.item(y, x, 2) * (1.0 - weight) + secondImage.item(y, x, 2) * weight

                copyImg.itemset((y, x, 0), blendingPixelBlue)
                copyImg.itemset((y, x, 1), blendingPixelGreen)
                copyImg.itemset((y, x, 2), blendingPixelRed)

    return copyImg

def geraMarcaDagua(imagem1, fundo):

    #Carregando as duas games
    mark = cv2.imread(imagem1)
    background = cv2.imread(fundo)

    #Redimensionando a imagem menor
    mark = resizeImage(mark, 90)

    #Imagem que fica por trás, imagem da frente, posição x e y da imagem da frente
    finalImageUm = addImageOverlay(background, mark, 460, 30)

    #Adicionando o Blending
    finalImage = addBlendingEffect(finalImageUm, background, 0.5)

    showImage(finalImage)
    cv2.imwrite("morte.png", finalImage)

def main():
    geraMarcaDagua("img/oi.jpg", "img/bug.png")

if __name__ == "__main__":
    main()
