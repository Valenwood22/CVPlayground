import cv2
import numpy as np


# # Side by side
# img = cv2.imread("Resources/TESO.jpg")

# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)



# # Warp Perspective
# img = cv2.imread("Resources/TESO.jpg")
#
# width, height = 250, 350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#
# cv2.imshow("Image", img)
# cv2.imshow("Output",imgOutput)



# # Drawing shapes
# img = np.zeros((512,512,3), np.uint8)
#
# # img[:] = 255,0,0 #Color it blue
#
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# cv2.rectangle(img, (0,0), (250,350),(0,0,255),cv2.FILLED)
# cv2.circle(img, (400,50),30,(255,255,0),5)
# cv2.putText(img,"  OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
#
# cv2.imshow("Image", img)



# # Resizing and cropping
# img = cv2.imread("Resources/TESO.jpg")
# imgResize = cv2.resize(img,(300,200))
#
# imgCropped = img[0:200, 200:500]
#
# cv2.imshow("Image", img)
# cv2.imshow("Image Resize", imgResize)
# cv2.imshow("Image Cropped", imgCropped)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# # Function for image Stacking
# img = cv2.imread('Resources/TESO.jpg')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img]))
# cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)