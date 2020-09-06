import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

cap.set(3,frameWidth) # Screen size
cap.set(4,frameHeight) # Screen size
cap.set(10,150) # Brightness

colors = [[48,31,9,98,140,255]]
colorValues = [[0,204,102]] ## USE BGR (NOT RGB)

points = [] # [x,y,colorid]

def findColor(img, colors, colorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    lower = np.array(colors[0][0:3])
    upper = np.array(colors[0][3:6])
    mask = cv2.inRange(imgHSV,lower,upper)
    x, y = getContours(mask)
    cv2.circle(imgResult,(x,y),10,colorValues[0],cv2.FILLED)
    if x != 0 and y != 0:
        newpoints.append([x,y,count])
    #cv2.imshow("img",mask)
    return newpoints



def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # Detects the outer corners
    x = y = w = h = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area > 300:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y



def drawOnCanvas(points, colorValues):
    for point in points:
        cv2.circle(imgResult,(point[0],point[1]),10,colorValues[point[2]],cv2.FILLED)


print("Running at", cap.get(cv2.CAP_PROP_FPS), "fps")
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findColor(img, colors, colorValues)
    if len(newpoints) !=0:
        for newP in newpoints:
            points.append(newP)
    if len(points)!=0:
        drawOnCanvas(points, colorValues)

    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
