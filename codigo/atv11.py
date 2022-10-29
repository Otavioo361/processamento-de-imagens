import numpy as np
import cv2

ESC_KEY = 27

cap = cv2.VideoCapture('teste3.mp4') #Carregando o video

#Função que manipula os valores da trackbar
def setLimitsOfTrackbar():
    hue = {}   #Declarando um dicionario com 2 "gavetas"
    hue["min"] = cv2.getTrackbarPos("Min Hue", trackbarWindow)
    hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    if hue["min"] > hue["max"]:  #Tratando o problema do mínimo ultrapassar o máximo
        cv2.setTrackbarPos("Max Hue", trackbarWindow, hue["min"])
        hue["max"] = cv2.getTrackbarPos("Max Hue", trackbarWindow)

    sat = {}    #Declarando um dicionario com 2 "gavetas"
    sat["min"] = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
    sat["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    if sat["min"] > sat["max"]: #Tratando o problema do mínimo ultrapassar o máximo
        cv2.setTrackbarPos("Max Saturation", trackbarWindow, sat["min"])
        sat["max"] = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

    val = {}    #Declarando um dicionario com 2 "gavetas"
    val["min"] = cv2.getTrackbarPos("Min Value", trackbarWindow)
    val["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    if val["min"] > val["max"]: #Tratando o problema do mínimo ultrapassar o máximo
        cv2.setTrackbarPos("Max Value", trackbarWindow, val["min"])
        val["max"] = cv2.getTrackbarPos("Max Value", trackbarWindow)

    return hue, sat, val

def computeTracking(frame, hue, sat, val):

    #Transforma a imagem de RGB para HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Definir os intervalos de cores que vão aparecer na imagem final
    lowerColor = np.array([hue['min'], sat["min"], val["min"]])
    upperColor = np.array([hue['max'], sat["max"], val["max"]])

    #Marcador pra saber se o pixel pertence ao intervalo ou não
    mask = cv2.inRange(hsvImage, lowerColor, upperColor)

    #Aplica máscara que "deixa passar" pixels pertencentes ao intervalo, como filtro
    #bitwise_and(source1_array,source2_array,destination_array,mask)
    #transforma a imagem/video para bit a bit e joga nos dois arrays como forma de mesclar,
    #Mas como só preciso da transformação jogo dentro do proprio frame
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #Aplica limiarização
    gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    #Para cada pixel o valor limite é aplicado no caso um limite binario
    _,gray = cv2.threshold(gray, 0, 230, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #Encontra pontos que circundam regiões conexas (contour)
    #cv2.retr_list e cv2.CHAIN_APPROX_SIMPLE sao usados para fazer uma detecção de contornos
    contours, hierarchy = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    #Se existir contornos
    if contours:
        #Retornando a área do primeiro grupo de pixels brancos
        maxArea = cv2.contourArea(contours[0])
        contourMaxAreaId = 0
        i = 0

        #Para cada grupo de pixels branco
        for cnt in contours:
            #Procura o grupo com a maior área
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                contourMaxAreaId = i
            i += 1

        #Achar o contorno com maior área em pixels
        cntMaxArea = contours[contourMaxAreaId]

        #Retorna um retângulo que envolve o contorno em questão
        #Que faz um delimitador de pontos ou pixels diferente de zero de imagens de escala cinza
        xRect, yRect, wRect, hRect = cv2.boundingRect(cntMaxArea)

        #Desenha caixa envolvente com espessura 3
        cv2.rectangle(frame, (xRect, yRect), (xRect + wRect, yRect + hRect), (255, 255, 0), 2)

    return frame, gray

trackbarWindow = "trackbar window" #Dando nome para janela grafica
cv2.namedWindow(trackbarWindow)    #Criando a janela grafica

def onChange(val):
    return

#Criando as trackbars
cv2.createTrackbar("Min Hue", trackbarWindow, 0, 255, onChange)  #Mínimo e maximo
cv2.createTrackbar("Max Hue", trackbarWindow, 13, 255, onChange)

cv2.createTrackbar("Min Saturation", trackbarWindow, 0, 255, onChange)
cv2.createTrackbar("Max Saturation", trackbarWindow, 255, 255, onChange)

cv2.createTrackbar("Min Value", trackbarWindow, 43, 255, onChange)
cv2.createTrackbar("Max Value", trackbarWindow, 255, 255, onChange)

#Associando as trackbars criadas na janela, retorna oque esta marcado na barrinha
min_hue = cv2.getTrackbarPos("Min Hue", trackbarWindow)
max_hue = cv2.getTrackbarPos("Max Hue", trackbarWindow)

min_sat = cv2.getTrackbarPos("Min Saturation", trackbarWindow)
max_sat = cv2.getTrackbarPos("Max Saturation", trackbarWindow)

min_val = cv2.getTrackbarPos("Min Value", trackbarWindow)
max_val = cv2.getTrackbarPos("Max Value", trackbarWindow)

while True:
    success, frame = cap.read()  #Retorna cada frame do video, sucess diz se o carregamento foi bem sucessido

    hue, sat, val = setLimitsOfTrackbar()
    frame, gray = computeTracking(frame, hue, sat, val)

    cv2.imshow("mascara", gray)
    cv2.imshow("video", frame)

    if cv2.waitKey(10) & 0xFF == ord('q') or 0xFF == ESC_KEY:
        break

cap.release()
cv2.destroyAllWindows()