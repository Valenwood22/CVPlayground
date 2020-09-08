import cv2

#########################################
frameWidth = 820
frameHeight = 600
object = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
minArea = 500
color = (255,255,255)
#########################################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0

while True:
    success, img = cap.read()
    imagGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = object.detectMultiScale(imagGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, x + h), (255, 255, 255), 2)
            cv2.putText(img, "face", (x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI", imgRoi)

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/Face_"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,0,0),cv2.FILLED)
        cv2.putText(img, "Scan Saved",(150,265),cv2.FONT_HERSHEY_COMPLEX
                    ,2,(255,0,225),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1


