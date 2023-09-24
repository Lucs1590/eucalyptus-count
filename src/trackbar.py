   #!/usr/bin/python
# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np 

def update(*arg):
	h0 = cv2.getTrackbarPos('h min', 'controle')
	h1 = cv2.getTrackbarPos('h max', 'controle') #***********************************************************
	s0 = cv2.getTrackbarPos('s min', 'controle')#*************************************************************************************************************** 
	s1 = cv2.getTrackbarPos('s max', 'controle') #***********************************************************
	v0 = cv2.getTrackbarPos('v min', 'controle')#***************************************************************************************************************
	v1 = cv2.getTrackbarPos('v max', 'controle') #***********************************************************
	#thrs = cv2.getTrackbarPos('thresh','control')
	lower = np.array((h0,s0,v0))
	upper = np.array((h1,s1,v1))
	mask = cv2.inRange(hsv, lower, upper)
	cv2.imshow('mask', mask)

def main():
	cv2.namedWindow('controle', 0)
	#trackbar(nome controle, janela, default, max, funcao)
	cv2.createTrackbar('h min', 'controle', 0, 255, update)
	cv2.createTrackbar('h max', 'controle', 0, 255, update)#****************************************************************************************************************
	cv2.createTrackbar('s min', 'controle', 0, 255, update)#***************************************************************************************************************
	cv2.createTrackbar('s max', 'controle', 0, 255, update)#****************************************************************************************************************
	cv2.createTrackbar('v min', 'controle', 0, 255, update)#***************************************************************************************************************
	cv2.createTrackbar('v max', 'controle', 0, 255, update)#****************************************************************************************************************
	im = cv2.resize(src, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
	cv2.imshow('controle',im)
	update()
	while 1:
		ch = cv2.waitKey(30)
		if (ch == 27):
			cv2.destroyAllWindows()
			break

if __name__ == '__main__':
	import sys
	try:
		fn = sys.argv[1]
		print("parametro:", fn)
	except:
		fn = 'images/euca_net1.jpg'
		
	print("file:", fn)	
	src = cv2.imread(fn)
	print("shape:", src.shape)
	#resize(imagem_entrada, None, (x,y), flag interpolacao  )
	#resize(imagem_entrada, None, scala x, escala y, flag interpolacao  )
	#src = cv2.resize(src, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_CUBIC)
	print("resized shape:", src.shape)
	hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
	main()
	