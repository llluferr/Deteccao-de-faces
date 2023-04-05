import cv2

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imagem = cv2.imread("imagens/tiao.jpg")
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces_detectadas = detector.detectMultiScale(imagem_cinza)
print(faces_detectadas)

cv2.imshow("Tiao, o Criador", imagem_cinza)
cv2.waitKey()