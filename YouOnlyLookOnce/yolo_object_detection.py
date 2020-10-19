import cv2
import numpy as np
import glob
import random

'''
                    =========== Experiment Notes 10/18/2020 ============
1. This script is currently using the weights from the hand_five data set using 118 images
2. It was trained online using google Colaboratory, Average loss < 0.4, ~2.5  hours of training
3. Results are promising but far from perfect. 99.15% accuracy on training data, 37.5% accuracy on unseen data (sample size of 16)
4. What we need to do going forward
    a. Collect a larger data set minimum 400 images per gesture
    b. Train it longer on Colaboratory full 12 hours, Average loss < 0.01
    c. Collect a larger set of unseen data minimum 100 images per gesture
    d. Settings like score_threshold, nms_threshold, and confidence threshold can be adjusted and optimized
'''


# Load Yolo
net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3_testing.cfg")

# Name custom object
classes = ["hand_five"]

# Images path
images_path = glob.glob(r"C:\Users\treeb\OneDrive\Desktop\SampleHand DataSet\*.png")

# Unseen data: r"C:\Users\treeb\OneDrive\Pictures\Camera Roll\hand_five\*.jpg"
# Training data: r"C:\Users\treeb\OneDrive\Desktop\SampleHand DataSet\*.png"

layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Insert here the path of your images
random.shuffle(images_path)
# loop through all the images
for img_path in images_path:
    # Loading image
    img = cv2.imread(img_path)
    # img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
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
                print(class_id)
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


    cv2.imshow("Image", img)
    key = cv2.waitKey(0)

cv2.destroyAllWindows()