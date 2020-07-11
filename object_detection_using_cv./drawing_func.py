import cv2
import numpy as np

#img = cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)


img = cv2.line(img,(0,0),(100,100),(255,0,0), 5)# to draw blue line
img = cv2.arrowedLine(img,(0,0),(255,255),(255,0,0), 5)


#img = cv2.rectangle(img,(271,0),(50,50),(255,0,0), 5)# to draw rect
img = cv2.circle(img,(50,50),10, (0,255,0),-1) #to draw circle and fill up green color
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'opencv',(60,60),font, 4, (255,255,255),10,cv2.LINE_AA)# to draw text on images


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
