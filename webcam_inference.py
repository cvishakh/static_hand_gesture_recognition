#Import necessary libraries
import torch
import cv2
from yolov5 import detect  # Make sure to have the yolov5 repo in your path
from pathlib import Path
import pathlib

#Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available! GPU is being used.")
    print("Current device:", torch.cuda.get_device_name(0))
else:
    print("CUDA is not available. Running on CPU.")

pathlib.PosixPath = pathlib.WindowsPath
#Load custom trained YOLOv5s model
model = torch.hub.load('yolov5', 'custom', path='C:/Users/visha/Documents/ProjectThesis/yolov5/best.pt', source='local', device='cpu') #change to cuda, if gpu

#Initialize the webcam
cap = cv2.VideoCapture(0)
#Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

#Main loop to capture frames and perform inference
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    #Perform inference on the frame
    results = model(frame)

    #Draw bounding boxes and labels on the frame
    annotated_frame = results.render()[0]  # Use results.render() to get the annotated frame

    #Display the annotated frame
    cv2.imshow("Static Gesture Recognition Inference", annotated_frame)

    #Press 'q' to quit the live webcam feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the webcam and close the display window
cap.release()
cv2.destroyAllWindows()