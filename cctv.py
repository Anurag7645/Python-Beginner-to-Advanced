import cv2
import numpy as np
import requests

# Load pre-trained models
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
theft_model = cv2.dnn.readNet('ssd_mobilenet_v3_large_coco.pb', 'ssd_mobilenet_v3_large_coco.pbtxt')

# Initialize video stream
cap = cv2.VideoCapture(0)

while True:
    # Read frame from video stream
    ret, frame = cap.read()
    
    # Detect faces in the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Detect theft events in the frame
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    theft_model.setInput(blob)
    detections = theft_model.forward()
    
    # Iterate through detected objects and filter for theft events
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            if class_id == 1: # Person class
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype
