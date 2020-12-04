__authors__ = ["Joshua Gisi"]
__copyright__ = ""
__version__ = "Experimental"
__email__ = "Joshua.Gisi@ndus.edu"
__status__ = "Development"


import cv2
import numpy as np
import glob
import random

# Load Yolo
net = cv2.dnn.readNet("yolo-obj_last.weights", "yolo-obj.cfg")

# Name custom object
classes = ["RH_Zero","RH_One","RH_Two","RH_Three","RH_Four","RH_Five",]

# Images path
images_path = glob.glob(r"C:\Users\treeb\OneDrive\Pictures\Camera Roll\hand_five\*.jpg")
# C:\Users\treeb\OneDrive\Desktop\images\*jpg
# Unseen data: r"C:\Users\treeb\OneDrive\Pictures\Camera Roll\hand_five\*.jpg"
# Training data: r"C:\Users\treeb\OneDrive\Desktop\SampleHand DataSet\*.png"

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Insert here the path of your images
random.shuffle(images_path)

cap = cv2.VideoCapture(0)
cap.set(3, 1280) # Screen size
cap.set(4,1024) # Screen size
cap.set(10,100) # Brightness
while True:
    success, img = cap.read()

    height, width, channels = img.shape

    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing information on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.3) # defaults 0.4 0.5
    print(indexes)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 2)


    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


#
# # loop through all the images
# for img_path in images_path:
#     # Loading image
#     img = cv2.imread(img_path)
#     img = cv2.resize(img, None, fx=1, fy=1)
#     height, width, channels = img.shape
#
#     # Detecting objects
#     blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
#
#     net.setInput(blob)
#     outs = net.forward(output_layers)
#
#     # Showing information on the screen
#     class_ids = []
#     confidences = []
#     boxes = []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.3:
#                 # Object detected
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)
#
#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)
#
#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)
#
#
#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.3) # defaults 0.4 0.5
#     print(indexes)
#     font = cv2.FONT_HERSHEY_PLAIN
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(img, label, (x, y + 30), font, 3, color, 2)
#
#
#     cv2.imshow("Image", img)
#     key = cv2.waitKey(0)
#
# cv2.destroyAllWindows()