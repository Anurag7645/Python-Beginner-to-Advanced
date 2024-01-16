import cv2
import dlib
import numpy as np
import tensorflow as tf

# Load the pre-trained face detector model
face_detector = dlib.get_frontal_face_detector()

# Load the pre-trained theft detection model (e.g., SSD or YOLO)
theft_detector = cv2.dnn.readNetFromTensorflow('theft_detection_model.pb')

# Load the video feed from CCTV
cap = cv2.VideoCapture('live_cctv_feed.mp4')

# Loop through the frames of the video
while True:
    ret, frame = cap.read()

    if not ret:
        # End of video
        break

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_detector(gray)

    # Loop through the detected faces
    for rect in faces:
        # Extract face region
        x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
        face_roi = frame[y:y+h, x:x+w]

        # Convert the face region to blob for theft detection
        blob = cv2.dnn.blobFromImage(face_roi, size=(300, 300), swapRB=True)

        # Pass the face region through the theft detection model
        theft_detector.setInput(blob)
        detections = theft_detector.forward()

        # Loop through the detections
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # Check if the detection is above a certain confidence threshold
            if confidence > 0.5:
                # Report theft to the police
                print("Theft detected! Reporting to the police...")

                # Capture an image of the theft event for evidence
                cv2.imwrite('theft_event.jpg', frame)

                # Send notification to the police or security personnel

    # Display the frame with detections
    cv2.imshow('CCTV Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
