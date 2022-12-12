import cv2
import numpy as np
from matplotlib import pyplot as plt


def histoCo():
    img = cv2.imread('img/doidera.jpg') #Carregando a imagem colorida

    #Criando uma lista com 3 elementos
    color = ('b', 'g', 'r')

    #"col" vai receber b, depois g, depois r
    #"enumerate()" é util na passagem de parâmetros para construir cada histograma
    for i, col in enumerate(color): #For que vai iterar para cada canal
        mascara=None
        histograma = cv2.calcHist([img], [i], mascara, [255], [0,255]) #Função que gera os 3 histogramas separados.
        #                         image   id    hist     intervalos
        plt.plot(histograma, color = col)    #Função que constroi o histograma definido, para o canal de cor específico
        #Obtenha ou defina os limites x dos eixos atuais.
        plt.xlim([0,255])    #Definindo os limites em relação a X desse histograma

    #Exibindo a imagem e o histograma
    cv2.imshow("Imagem original", img)
    plt.show()

    cv2.waitKey(0) #Tecla Q
    cv2.destroyAllWindows()

histoCo()