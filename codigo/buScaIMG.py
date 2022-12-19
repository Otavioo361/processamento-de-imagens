
#https://theailearner.com/tag/cv2-comparehist/
#https://docs.opencv.org/3.4/d6/dc7/group__imgproc__hist.html#gga994f53817d621e2e4228fc646342d386ad75f6e8385d2e29479cf61ba87b57450
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as mt


#Funcao que recebe 5 imagens e compara os seus histogramas com a primeira
def comparaHistograma(S1,S2,D1,D2,D3):
    #Calculando os histogramas de todas as imagens atraves do "cv2.calcHist"
    #cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
    histS1 = cv2.calcHist([S1], [0], None, [256], [0, 256])
    histS2 = cv2.calcHist([S2], [0], None, [256], [0, 256])
    histD1 = cv2.calcHist([D1], [0], None, [256], [0, 256])
    histD2 = cv2.calcHist([D2], [0], None, [256], [0, 256])
    histD3 = cv2.calcHist([D3], [0], None, [256], [0, 256])

    #---------------------------------------S1 COM S2--------------------------------------
    print("----------------------------------------------")
    print("*S1 com S2\n")
    #Correlação
    #quando as imagens são iguais o resultado é 1
    correlacaoS1S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,S2)  :", correlacaoS1S2)

    #Chi-Square
    
    chiSquareS1S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,S2)  :", chiSquareS1S2)

    #Bhattacharyya
    #bhattacharyya  histogramas iguais o resultado é  aproximado de 1
    bhattacharyyaS1S2 = cv2.compareHist(histS1, histS2, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,S2):", bhattacharyyaS1S2)

    distanciaS1S2 = 0
    distS1S2 = float(distanciaS1S2)
                #raiz quadrada numero elevado
    distS1S2 = mt.sqrt(pow(correlacaoS1S2,2) + pow(chiSquareS1S2,2) + pow(bhattacharyyaS1S2,2))
    print("Distancia(S1,S2)   :", distS1S2)
    print("----------------------------------------------")
    #--------------------------------------------------------------------------------------

    #---------------------------------------S1 COM D1--------------------------------------
    print("*S1 com D1\n")
    #Correlação
    correlacaoS1D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,D1)  :", correlacaoS1D1)

    #Chi-Square
    chiSquareS1D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,D1)  :", chiSquareS1D1)

    #Bhattacharyya
    bhattacharyyaS1D1 = cv2.compareHist(histS1, histD1, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,D1):", bhattacharyyaS1D1)

    distanciaS1D1 = 0
    distS1D1 = float(distanciaS1D1)

    distS1D1 = mt.sqrt(pow(correlacaoS1D1,2) + pow(chiSquareS1D1,2) + pow(bhattacharyyaS1D1,2))
    print("Distancia(S1,D1)   :", distS1D1)
    print("----------------------------------------------")
    #--------------------------------------------------------------------------------------

    #---------------------------------------S1 COM D2--------------------------------------
    print("*S1 com D2\n")
    #Correlação
    correlacaoS1D2 = cv2.compareHist(histS1, histD2, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,D2)  :", correlacaoS1D2)

    #Chi-Square
    chiSquareS1D2 = cv2.compareHist(histS1, histD2, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,D2)  :", chiSquareS1D2)

    #Bhattacharyya
    bhattacharyyaS1D2 = cv2.compareHist(histS1, histD2, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,D2):", bhattacharyyaS1D2)

    distanciaS1D2 = 0
    distS1D2 = float(distanciaS1D2)

    distS1D2 = mt.sqrt(pow(correlacaoS1D2,2) + pow(chiSquareS1D2,2) + pow(bhattacharyyaS1D2,2))
    print("Distancia(S1,D2)   :", distS1D2)
    print("----------------------------------------------")
    #--------------------------------------------------------------------------------------

    #---------------------------------------S1 COM D3--------------------------------------
    print("*S1 com D3\n")
    #Correlação
    correlacaoS1D3 = cv2.compareHist(histS1, histD3, cv2.HISTCMP_CORREL)
    print("Correlacao(S1,D3)  :", correlacaoS1D3)

    #Chi-Square
    chiSquareS1D3 = cv2.compareHist(histS1, histD3, cv2.HISTCMP_CHISQR)
    print("Chi-Square(S1,D3)  :", chiSquareS1D3)

    #Bhattacharyya
    bhattacharyyaS1D3 = cv2.compareHist(histS1, histD3, cv2.HISTCMP_BHATTACHARYYA)
    print("Bhattacharry(S1,D3):", bhattacharyyaS1D3)

    distanciaS1D3 = 0
    distS1D3 = float(distanciaS1D3)

    distS1D3 = mt.sqrt(pow(correlacaoS1D3,2) + pow(chiSquareS1D3,2) + pow(bhattacharyyaS1D3,2))
    print("Distancia(S1,D3)   :", distS1D3)
    print("----------------------------------------------")
    #--------------------------------------------------------------------------------------

    #Ver qual distancia é menor
    vetAux = np.array([distS1S2, distS1D1, distS1D2, distS1D3]);
    #Retorna o mínimo de uma matriz.
    min = np.amin(vetAux)
    print(vetAux)

    #Imprimindo a respostas na Tela
    if(min == distS1S2):
        print("A imagem S2 e a mais parecida com a S1.")
        cv2.imshow("imgs2",S2)

    if(min == distS1D1):
        print("A imagem D1 e a mais parecida com a S1.")
        cv2.imshow("imgD1",D1)

    if(min == distS1D2):
        print("A imagem D2 e a mais parecida com a S1.")
        cv2.imshow("imgD2",D2)

    if(min == distS1D3):
        print("A imagem D3 e a mais parecida com a S1.")
        cv2.imshow("imgD3",D3)

def main():

    #Carregando as imagens
    S1 = cv2.imread('img/S1.jpg')
    S2 = cv2.imread('img/S2.jpg')
    D1 = cv2.imread('img/D1.jpg')
    D2 = cv2.imread('img/D2.jpg')
    D3 = cv2.imread('img/D3.jpg')

  

    comparaHistograma(S1,S2,D1,D2,D3)    
    cv2.imshow("Imagem original", S1)
    plt.show()

    cv2.waitKey(0)  #Tecla Q
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
