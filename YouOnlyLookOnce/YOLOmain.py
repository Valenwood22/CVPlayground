__authors__ = ["Joshua Gisi"]
__copyright__ = ""
__version__ = "Experimental"
__email__ = "Joshua.Gisi@ndus.edu"
__status__ = "Development"

import cv2
import numpy as np
# hand Data set https://lttm.dei.unipd.it/downloads/gesture/

# Load YOLO
net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3.cfg")



with open("handv1.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# Loading image
img = cv2.imread("data/family.png")
# img = cv2.resize(img, None, fx=0.4, fy=0.4) # Resize the image to fit on the screen
height, width, channels = img.shape

# Separating the image into RBG channels
blob = cv2.dnn.blobFromImage(img, 0.00392, (416,416), (0,0,0), True, crop=False)

# Take a look the the blob
# for b in blob:
#     for i, img_blob in enumerate(b):
#         cv2.imshow(str(i), img_blob)

net.setInput(blob) # setting up the network
outs = net.forward(output_layers) #feed in the image

# Showing information on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5: # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # cv2.circle(img, (center_x, center_y), 10, (0,255,0), 2) # Center
            # Rectangle coordinates
            x = int(center_x-w/2)
            y = int(center_y-h/2)

            boxes.append([x,y,w,h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
print(indexes)
number_objects_detected = len(boxes)
font = cv2.FONT_HERSHEY_DUPLEX
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        #print(label)
        cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),2)
        cv2.putText(img, label, (x, y-10), font, 1,(0,25,0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


