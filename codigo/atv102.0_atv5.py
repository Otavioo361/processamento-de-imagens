import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def showImage(img):
    img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    width = 1280
    hieght = 720
    channel = 3

    fps = 10
    sec = 10

    fourcc = cv2.VideoWriter_fourcc(*'MP42')

    video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))

    

    current_contrast = 0

    t = 0    #Variavel para entrar 
    g = 30   #Variavel para saida do brilho

    for frame_count in range(fps*sec):

        img = cv2.imread("img/oi.jpg")
        img_resize = cv2.resize(img, (width, hieght))

        #Inicia com a cor preta(o de brilho) ate 1 segundo
        if((frame_count >= 1) and (frame_count <= 10)):
			#convertScaleAbs=saturate\_cast<uchar>(|src(I)∗alpha+beta|)
			#Dimensiona, calcula valores absolutos e converte o resultado em 8 bits. 
			#Em cada elemento da matriz de entrada, a função convertScaleAbs executa três operações sequencialmente: dimensionamento, obtenção de um valor absoluto, 
			#conversão para um tipo de 8 bits sem sinal:
            img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t)
            video.write(img_resize)
            print(frame_count)

        #entrada do brilho
        if((frame_count >= 10) and (frame_count <= 20)):
            img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t)
            video.write(img_resize)
            t += 4
            current_contrast += 6
            print(frame_count)

        #Normal
        if((frame_count >= 20) and (frame_count <= 40)):
            img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t)
            video.write(img_resize)
            print(frame_count)

        #saida do brilho
        if((frame_count >= 40) and (frame_count <= 50)):
            img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t)
            video.write(img_resize)
            t -= 4
            current_contrast -= 6
            print(frame_count)

        if((frame_count >= 50) and (frame_count <= 60)):
            img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t)
            video.write(img_resize)
            print(frame_count)

if __name__ == "__main__":
	main()
