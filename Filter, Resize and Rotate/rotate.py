import cv2


class Rotate:

	def rotate(self, img, angle)
		altura, largura = img.shape[0], img.shape[1]
		rotation_matrix = cv2.getRotationMatrix2D((largura/2, altura/2), angle, 1)
		return cv2.warpAffine(img, rotation_matrix, (largura, altura))

	