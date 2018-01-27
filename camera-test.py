# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:59:43 2018

@author: Lambert Rosique
"""

import cv2

# Test if camera is detected by Python

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()