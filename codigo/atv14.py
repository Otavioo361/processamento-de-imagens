import cv2
import numpy as np
from matplotlib import pyplot as plt

def claro():
    imgBgr = cv2.imread("img/doidera.jpg")

    #Convertendo a imagem para HSV
    imgHsv = cv2.cvtColor(imgBgr, cv2.COLOR_BGR2HSV)
    #hsv(hue,saturação e brilho)
    imgHsv[:, :, 2] = cv2.equalizeHist(imgHsv[:, :, 2])# O canal V no espaço de cores HSV que deixa mais claro a imagem
    saida = cv2.cvtColor(imgHsv, cv2.COLOR_HSV2BGR) #Convertendo a imagem de volta para BGR    
    cv2.imwrite("equalizeHist.jpg",saida)

      #Criando uma lista com 3 elementos
    color = ('b', 'g', 'r')

    #"col" vai receber b, depois g, depois r
    #"enumerate()" é util na passagem de parâmetros para construir cada histograma
    for i, col in enumerate(color): #For que vai iterar para cada canal
        mascara=None
        histograma = cv2.calcHist([imgBgr], [i], mascara, [255], [0,255]) #Função que gera os 3 histogramas separados.        
        plt.plot(histograma, color = col)    #Função que constroi o histograma definido, para o canal de cor específico       
        #Obtenha ou defina os limites x dos eixos atuais.
        plt.xlim([0,255])    #Definindo os limites em relação a X desse histograma
        
        
    plt.show

    for i,col in enumerate(color):
        mascara=None
        histogramaClaro = cv2.calcHist([saida], [i], mascara, [255], [0,255]) #Função que gera os 3 histogramas separados.
        plt.plot(histogramaClaro, color= col)
        plt.xlim([0,255])


    #Exibindo a imagem e o histograma
    cv2.imshow("Imagem original", imgBgr)
    cv2.imshow("Imagem Clara",saida)
    plt.show()

    cv2.waitKey(0) #Tecla Q
    cv2.destroyAllWindows()
    
     
claro()
