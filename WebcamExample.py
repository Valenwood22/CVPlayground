import cv2

# # Importing an image
# img = cv2.imread("Resources/TESO.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# # Importing a video
# cap = cv2.VideoCapture("Resources/Bird_video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# Importing a video
cap = cv2.VideoCapture(0)
cap.set(3,640) # Screen size
cap.set(4,480) # Screen size
cap.set(10,100) # Brightness
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


