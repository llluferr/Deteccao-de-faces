import cv2

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imagem = cv2.imread("imagens/tiao.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces_detectadas = detector.detectMultiScale(imagem_cinza, scaleFactor=1.07)
print(faces_detectadas)
for x, y, l, a in faces_detectadas:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (0,0,255), 2)

cv2.imshow("Tiao, o Criador", imagem)
cv2.waitKey()