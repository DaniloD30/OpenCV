import cv2
import numpy as np

class Filter:

	def BGR2HSV(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	def gray(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	def bgr2xyz(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)

	def BGR2YCrCb(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

	def BGR2Luv(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2Luv)
	
	def BGR2HLS(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
	
	def BGR2Lab(self, img):
		return cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
	
	
	