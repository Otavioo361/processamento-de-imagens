import numpy as np
import cv2

# ESC
ESCAPE_KEY_ASCII = 27


def resizeImage(img, scalePercent):
    width = int(img.shape[1] * scalePercent / 100)
    height = int(img.shape[0] * scalePercent / 100)

    img = cv2.resize(img, (width, height))

    return img


def onChange(value):
    #print("valor alterado", value)
    pass


def mudando():
    # imagem carregada e sua cópia
    img = cv2.imread("img/bola.jpg")
    img = resizeImage(img, 64)
    copyimg = img.copy()

    # cria janela gráfica para inserir a imagem
    windowTitle = "Ajuste de Brilho e Contraste"
    cv2.namedWindow(windowTitle)

    # cria trackbar
    cv2.createTrackbar("Contraste", windowTitle, 100, 100, onChange)
    #nome da trackbar,associa  a barra com a janela ,valor inicial, metodo q vai ser chamado quando o usuario alterar os valores 
    cv2.createTrackbar("Brilho", windowTitle, 0, 200, onChange)

    before_contrast = 100
    #valor do contraste anterior
    update_contrast = False

    before_brightness = 0
    update_brightness = False
    #laço de looping infinito
    while True:
        current_contrast = cv2.getTrackbarPos("Contraste", windowTitle)
        #server para pegar a posição da barra do contraste
        current_brightness = cv2.getTrackbarPos("Brilho", windowTitle)
        #server para pegar a posição da barra do contraste

        # valor de contraste do trackbar foi alterado pelo usuário
        #Faz comparação para saber se  houve alteração no contraste
        if before_contrast != current_contrast:
            #MARCA quando o algoritmo tem q atualizar o contraste toda vez q o usuario mexer a barra
            update_contrast = True
            #before serve para ir atualizando o valor de contraste            
            before_contrast = current_contrast

        # valor de brilho do trackbar foi alterado pelo usuário
         #Faz comparação para saber se  houve alteração no  brilho
        if before_brightness != current_brightness:
            update_brightness = True
            before_brightness = current_brightness

            # se tiver sido marcado que é pra atualizar contraste ou brilho
        if update_contrast == True or update_brightness == True:

            # Método que aplica uma mudança em toda matriz alpha sendo contraste e o beta o brilho, variando de 0 a 1 0 é o minino e o 1 o maximo
            copyimg = cv2.convertScaleAbs(img, alpha=current_contrast / 100, beta=current_brightness)

            update_contrast = False
            #os dois updates feitos pois você não consegue modificar os dois ao mesmo tempo
            update_brightness = False

        cv2.imshow(windowTitle, copyimg)

        keyPressed = cv2.waitKey(1) & 0xFF # a cada 1 milisegundo ele ira "redesenhar" a imagem hexadecimal # cv2.waitKey(1) & 111111
        if keyPressed == ESCAPE_KEY_ASCII:
            break

    cv2.destroyAllWindows()


    
    
    
    
    
mudando()
