# DETECION DE COLORES Y CONTORNOS
import cv2
import numpy as np


def draw(mask, color):
    # Contorno de los objetos
    contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Se analiza cada objeto para sacar su contorno
    for c in contornos:
        area = cv2.contourArea(c)
        
        # Identificación del area mayor
        if area > 1000:
            
            # Punto central de cada objeto identificado
            M = cv2.moments(c)
            if (M["m00"] == 0):
                M["m00"] = 1
                
                
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])
            
            # Graficamos los contornos
            newContour = cv2.convexHull(c)
            
            # Graficamos un punto verde (radio = 7)
            cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
            
            # Mostramos las coordenadas del objeto
            cv2.putText(frame, '{}, {}'.format(x, y), (x+10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
            
            # Graficamos el contorno del objeto
            cv2.drawContours(frame, [newContour], 0, color, 3)
            
            
# Tipo de fuente
font = cv2.FONT_HERSHEY_SIMPLEX

# Puerto de nuestra camara
cam = cv2.VideoCapture(0)

# Máscara de colores a detectar
azulBajo = np.array([100, 100, 20], np.uint8)
azulAlto = np.array([125, 255, 255], np.uint8)

amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([40, 255, 255], np.uint8)

rojoBajo1 = np.array([0, 100, 20], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)

rojoBajo2 = np.array([175, 100, 20], np.uint8)
rojoAlto2 = np.array([179, 255, 255], np.uint8)

verdeBajo = np.array([50, 100, 20], np.uint8)
verdeAlto = np.array([80, 255, 255], np.uint8)

# Capturamos la imagen en todo momento
while True:
    # Inicia captura de imagen: True
    ret, frame = cam.read()
    
    # Si tenemos imagen
    if ret == True:
        
        # Pasamos de BGR a HSV
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Mascara color AZUL
        maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
        
        # Mascara color AMARILLO
        maskAmarillo = cv2.inRange(frameHSV, amarilloBajo, amarilloAlto)
        
        # Mascara color ROJO
        maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
        maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
        maskRojo = cv2.add(maskRojo1, maskRojo2)
        
        # Mascara color VERDE
        maskVerde = cv2.inRange(frameHSV, verdeBajo, verdeAlto)
        
        
        # Graficamos las mascaras de los colores a identificar
        draw(maskAzul, (255, 0, 0))
        draw(maskAmarillo, (0, 255, 255))
        draw(maskRojo, (0, 0, 255))
        draw(maskVerde, (0, 255, 0))
        
        # Mostramos la imagen de la camara
        cv2.imshow('frame', frame)
        
        
        # Detenemos la visualizacion con la letra s
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        
        
# Finalizamos la captura de video
cam.release()

# Cerramos todas las ventanas
cv2.destroyAllWindows()