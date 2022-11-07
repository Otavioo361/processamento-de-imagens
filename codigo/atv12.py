#Histograma PRETO E BRANCO
import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
Observações importantes no histograma(preto e branco):
    ->Os tons vão de preto até branco, da esquerda para a direita.
    ->Quanto maior o número de pontos a esquerda, mais pixels pretos tem a imagem.
    ->Quanto maior o número de pontos a direita, mais pixels brancos tem a imagem.
    ->Pixels no meio = tons de cinza
"""

def main():
    img = cv2.imread('img/bug.png', 0) #Carregando a imagem em preto e branco
    #ravel() pega a matriz 2d que componhe a imagem e converte em um vetor através de combinação
    #plt.hist precisa que a matriz se transforme em um vetor de uma dimensão os dados em x e contar o número de valores em cada compartimento e, em seguida, desenha a distribuição
    plt.hist(img.ravel(), 255, [0, 255]) #Segundo parametro define os pins. 255 afirma que tenho 1 bin por tom
    #Terceiro parametro, de qual tom em x até qual tom em x, irá representar no histograma

    #Mostrando o histograma e a imagem na tela
    cv2.imshow("Imagem original", img)
    plt.imshow(img)
    plt.show()
    cv2.waitKey(0)  #Tecla Q
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()