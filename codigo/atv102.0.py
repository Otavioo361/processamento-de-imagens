import cv2
import numpy as np 

#tarefa 5 ---------1 


def viodeo():
    #pre definindo o tamanho do video
	largura = 1280
	altura = 720
	channel = 3
    # pre setanto a quantidade para o video
	fps = 24
	sec = 10

	fourcc = cv2.VideoWriter_fourcc(*'XVID')
#
	video = cv2.VideoWriter('video.avi', fourcc, float(fps), (largura, altura))

	current_contrast = 0
	
	t = 0    #Variavel para entrar a imagem
	g = 30   #Variavel para acabar o video com a imagem
	
	for frame_count in range(fps*sec):
		
		img = cv2.imread("img/tia1.png")
        #redimensionando a imagem
		img_resize = cv2.resize(img, (largura, altura))

	#Inicia com a cor preta(o de brilho) ate 1 segundo
		if((frame_count >= 1) and (frame_count < 10)):
			# #Conversao da img para 8 bits para poder colocar no video onde beta é o brilho e o alpha e o contraste
		   img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = 0) 
		   video.write(img_resize)
		   print(frame_count)
		   
		#Entrada da imagem
		if((frame_count > 10) and (frame_count <= 30)):
		   img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = t) 
		   video.write(img_resize)
		   t += 13
		   
		#Normal
		if((frame_count > 30) and (frame_count < 80)):
		   video.write(img_resize)
		   
		#finalização do video
		if((frame_count > 80) and (frame_count <= 100)):
		   img_resize = cv2.convertScaleAbs(img_resize, alpha = current_contrast / 100, beta = g)
		   video.write(img_resize)
		   t -= 13
		   

viodeo()
