import numpy as np
import cv2
from mss import mss
from PIL import Image
import pygetwindow as gw

# print(gw.getAllTitles())
UE4Window = gw.getWindowsWithTitle('Second_screen')[0]
print(UE4Window.size)
print(UE4Window.bottomright)
print(UE4Window.topleft)


R_Cam_bounding_box = {'top': 24, 'left': -1920, 'width': 960, 'height': 580}
L_Cam_bounding_box = {'top': 24, 'left': -960, 'width': 960, 'height': 580}

sct = mss()

while True:
    R_sct_img = sct.grab(R_Cam_bounding_box)
    L_sct_img = sct.grab(L_Cam_bounding_box)
    cv2.imshow('Right Cam', np.array(R_sct_img))
    cv2.imshow('Left Cam', np.array(L_sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
