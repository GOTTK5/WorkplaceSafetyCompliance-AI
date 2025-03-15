


import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import base64
import os
import threading


if not os.environ.get("WATERMARK"):
    os.environ["WATERMARK"] = base64.b64encode("Original YOLOv8 PPE Detection Code by [GOTTK5]".encode()).decode()

class Obfuscated:
    @staticmethod
    def _hidden_message():
        encoded_message = os.environ.get("WATERMARK")
        return base64.b64decode(encoded_message).decode() if encoded_message else "Copied Code Detected! GOTTK5 "


model = YOLO("best.pt")


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("⚠️ Error: Couldn't access the webcam.")
    exit()


print(Obfuscated._hidden_message())


plt.ion() 
fig, ax = plt.subplots()
plt.gcf().canvas.manager.set_window_title(Obfuscated._hidden_message())

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Error: Couldn't fetch frame from webcam.")
        break

   
    results = model(frame)
    annotated_frame = results[0].plot()

  
    img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

  
    ax.clear()
    ax.imshow(img)
    ax.set_title(Obfuscated._hidden_message() )
    ax.axis("off")
    plt.pause(0.01) 

   
    if not plt.fignum_exists(fig.number):
        print("🚀 Video Closed! Regards KRUPPK5")
        break

cap.release()
