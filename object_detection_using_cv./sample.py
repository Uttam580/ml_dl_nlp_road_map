import cv2
img = cv2.imread('lena.jpg',0)
print(img)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k==27:# if user press escape key
    cv2.destroyAllWindows()
elif k ==ord('s'):
    cv2.imwrite('lena_cp.jpg',img)#to write the the image
    cv2.destroyAllWindows()