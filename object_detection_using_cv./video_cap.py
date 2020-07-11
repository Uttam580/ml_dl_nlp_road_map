import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') # to get fourcc code for video capturing 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))# outputfilename , fourccccode , no of frame , size 

print(cap.isOpened())
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))to get frame size and width 
       #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# to convert colour image to gray image 
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):# if user press q , break the loop 
         break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()