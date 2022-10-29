import cv2
import numpy as np
import os


def viodeo():
    #pre definindo o tamanho do video
	largura = 1280
	altura = 720
	channel = 3
    # pre setanto a quantidade para o video
	fps = 10
	sec = 20

	fourcc = cv2.VideoWriter_fourcc(*'MP42')

	video = cv2.VideoWriter('video.avi', fourcc, float(fps), (largura, altura))

	directry = 'home/otavio/Documentos/Github/processamento-de-imagens/codigo/img'

	current_contrast = 0
	
	t = 0    #Variavel para entrar a imagem
	g = 30   #Variavel para acabar o video com a imagem
	
	for tempo in range(fps*sec):
		
		img = cv2.imread("img/tia1.png")
        #redimensionando a imagem
		img_resize = cv2.resize(img, (largura, altura))

		#Inicia com a cor preta(o de brilho) ate 1 segundo
		if((tempo >= 1) and (tempo < 10)):
			#Conversao da img para 8 bits para poder colocar no video onde beta é o brilho e o alpha e o contraste
			img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = 0) 
			#preparando a imagem
			video.write(img_resize)
			
		   
		#Entrada da imagem
		if((tempo > 10) and (tempo <= 30)):
			img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t) 
			video.write(img_resize)
			
		   
		

		
		if((tempo > 80) and (tempo <= 100)):
			img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = g)
			video.write(img_resize)		   

viodeo()
