import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob



def showSingleImage(img, title, size):
    #               imagem,titulo,tamanho
    fig, axis = plt.subplots()

    axis.imshow(img, 'gray')
    axis.set_title(title)
    plt.show()

def showMultipleImages(imgsArray, titlesArray, size, x, y):
                        #imagens , titulos, tamanho quantidade x e quantidade no y
    if(x < 1 or y < 1):
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return
    elif(x == 1 and y == 1):
        showSingleImage(imgsArray, titlesArray)
        #exibe uma imagem
    elif(x == 1):
        #tratamento vertical
        fig, axis = plt.subplots(y )
        #                       quantas linhas,quantas colunas
        yId = 0
        for img in imgsArray:
            #axis[yid] anda no eixo y
            axis[yId].imshow(img, 'gray')
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId] )
                #       coloca o titulo no array adequado

            yId += 1
    elif(y == 1):
        #tratamento horizontal
        fig, axis = plt.subplots(1, x )
                                #só vai passar o total de linhas e colunas 
        fig.suptitle(titlesArray)
        #superior title, coloca o titulo no meio,centralizada
        yId = 0
        for img in imgsArray:
            axis[yId].imshow(img, 'gray')
            axis[yId].set_anchor('NW')
            axis[yId].set_title(titlesArray[yId] )

            yId += 1
    else:
        #grades 2 por 2 em diante
        fig, axis = plt.subplots(y, x )
                                #total de linha,total de coluna
        xId, yId, titleId = 0, 0, 0
        #contador de xid,contador de y id e contador de titulos separadamente
        for img in imgsArray:
            axis[yId, xId].set_title(titlesArray[titleId] )
            #colocando titulo em cada imagem com suas configurações
            axis[yId, xId].set_anchor('NW')
            axis[yId, xId].imshow(img, 'gray')
            if(len(titlesArray[titleId]) == 0):
                axis[yId, xId].axis('off')

            titleId += 1
            xId += 1
            if xId == x:
                xId = 0
                yId += 1
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    folder = 'maps/*'
    image_files_list = glob.glob(folder)

    #Criando as variaveis para as imagens usando a lista do glob
    cartaGetulio = image_files_list[0]
    mapa_1 = image_files_list[1]
    mapa_2 = image_files_list[2]
    mapa_3 = image_files_list[3]

    #Carregando as imagens
    carta_cinza = cv2.imread(cartaGetulio, 0)
    mapa_1_cinza = cv2.imread(mapa_1, 0)
    mapa_2_cinza = cv2.imread(mapa_2, 0)

    eq = cv2.equalizeHist(mapa_2_cinza)
    #histograma

    mapa_3_cinza = cv2.imread(mapa_3, 0)    

    block_size = 171 #Tamanho da janela em que vao se calcular as regioes, quanto maior mais ele vai considerar
    C = 120 #
    


    ret, thresh_img = cv2.threshold(carta_cinza, 180, 255, cv2.THRESH_BINARY)  # binary explicada em baixo.
                                                #preto #branco
    #ret retorna a limiarização  e thresh img a imagem limiarizada
    #               aplica a limiarização,nome da imagem,limiar(min), valor do tom acima do limiar para todos que tiverrem igual ou acima ficar branco(255)
    #limiarização, separação das cores. Quem tiver abaixo vai ficar preto, quem estiver acima fica branco                              
    ret, thresh_img1 = cv2.threshold(mapa_1_cinza, 180, 255, cv2.THRESH_BINARY)  #Vai precisar aplicar um filtro para remover as linha
    medianImg = cv2.medianBlur(thresh_img1, 5)
    #Desfoca uma imagem usando o filtro mediano.
    #A função suaviza uma imagem usando o filtro mediano com a abertura ksize×ksize. Cada canal de uma imagem multicanal é processado independentemente. A operação no local é suportada.
  




    imgAdapMean_3 = cv2.adaptiveThreshold(eq, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)
                                            #img,valormax,configuração,                                            #faz a media e deduz em C
                                                        #Soma ponderada das gaussianas atraves de  uma formula abaixo fica preto e acima fica branco
    _, imgNormThresh_3 = cv2.threshold(mapa_3_cinza, 40, 255, cv2.THRESH_BINARY)



    imgsArray = [thresh_img,  medianImg, imgAdapMean_3, imgNormThresh_3]
    titlesArray = ['THRESH_BINARY', 'THRESH_BINARY', 'ADAPTIVE_THRESH_MEAN_C', 'THRESH_BINARY']
    #                                                   #adaptativa permite que a imagem dividida tenha um limiar proprio. baseada em média pegando a regiao da imagem e calculando sua média,soma e divide.Abaixo da media vai ficar preto e acima branco
    showMultipleImages(imgsArray, titlesArray, (20, 16), 2, 2)



if __name__ == "__main__":
    main()
