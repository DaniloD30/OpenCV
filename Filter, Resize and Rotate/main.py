import cv2
from rotate import Rotate 
from filter import Filter 

if __name__ == '__main__':
	'''
	#Rotacionar um quadrado 90 graus, não tera bordas pretas
	#Rotacionar uma imagem qualquer, em 180 graus, nao tera bordas pretas
	# Transformar a imagem em um quadrado (Largura == altura), solucionou
	# o problema das bordas pretas, nao fotos rotacionadas em 90 graus
	# load the image
	'''
	img = cv2.imread("sloughy-pressure-ulcer-0025.jpg")
	angle = 100
	
	imagemQuadrada = cv2.resize(img,(img.shape[1],img.shape[1]),interpolation=cv2.INTER_AREA)
	r = Rotate()
	f = Filter()
	rotatee = r.rotate(imagemQuadrada, angle)
	
	filtro1 = f.BGR2HSV(img)
	filtro2  = f.gray(img)
	filtro3  = f.bgr2xyz(img)
	filtro4  = f.BGR2YCrCb(img)
	filtro5  = f.BGR2Luv(img)
	filtro6  = f.BGR2HLS(img)
	filtro7  = f.BGR2Lab(img)
	
	cv2.imshow("Filter", filtro1 )
	cv2.imshow("Gray", filtro2 )
	cv2.imshow("COLOR_BGR2XYZ", filtro3 )
	cv2.imshow("BGR2YCrCb", filtro4 )
	cv2.imshow("BGR2Luv", filtro5 )
	cv2.imshow("BGR2HLS", filtro6 )
	cv2.imshow("BGR2Lab", filtro7 )
	
	cv2.imshow('Rotate', rotatee)
	cv2.imshow('Original', img)
	cv2.imshow("resize", imagemQuadrada)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
