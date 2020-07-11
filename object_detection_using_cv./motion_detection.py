import cv2
import numpy as np
cap = cv2.VideoCapture('vtest.avi') # to load video 

ret ,frame1= cap.read()# reading frame1
ret ,frame2= cap.read()# reading frame2

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)# to find differnce between two frame
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)#to convert into gray scale
    blur = cv2.GaussianBlur(gray,(5,5),0)# blur gray scale frame ,(frame, kernelsize, sigma value)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)#to find thresh (source,thresholdvalue,maxthreshold, type)
    dilated = cv2.dilate(thresh,None,iterations=3)# dialte the threshold images in all , to find better contour
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #to find contours on dialted images(source, type, method )

    #applying boundary on moving object 
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 700:# if countor area is greater than 700 then only apply boundary 
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)#applying rect boundary on moving object
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)# put text on frame 


    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)# to apply contours on frame

    cv2.imshow("feed", frame1)#
    frame1 = frame2
    ret, frame2 = cap.read()# reading new frame into 

    if cv2.waitKey(40) == 27:
        break


cv2.destroyAllWindows()#destroy the window 
cap.release()#release the resource
