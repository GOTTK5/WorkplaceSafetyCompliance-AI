

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import yt_dlp  
import pafy  
import base64
import os


if not os.environ.get("WATERMARK"):
    os.environ["WATERMARK"] = base64.b64encode("Original YOLOv8 PPE Detection Code by [GOTTK5]".encode()).decode()

class Obfuscated:
    @staticmethod
    def _hidden_message():
        encoded_message = os.environ.get("WATERMARK")
        return base64.b64decode(encoded_message).decode() if encoded_message else "Copied Code Detected! GOTTK5 "


model = YOLO("best.pt")


video_url = "https://youtu.be/OPs4MQOlZAQ?feature=shared"  

ydl_opts = {"format": "best"}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    video_url = info_dict["url"]

cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("⚠️ Error: Couldn't access the YouTube video.")
    exit()


print(Obfuscated._hidden_message())


frame_rate = 2 
frame_count = 0


plt.ion() 
fig, ax = plt.subplots()
plt.gcf().canvas.manager.set_window_title(Obfuscated._hidden_message())

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Error: Couldn't fetch frame from YouTube video.")
        break

    frame_count += 1
    
   
    if frame_count % frame_rate != 0:
        continue

   
    results = model(frame)
    annotated_frame = results[0].plot()

  
    img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    
    ax.clear()
    ax.imshow(img)
    ax.set_title(Obfuscated._hidden_message())
    ax.axis("off")
    plt.pause(0.01)

   
    if not plt.fignum_exists(fig.number):
        print("🚀 Video Closed! Exiting...")
        break


cap.release()
plt.close()


print(Obfuscated._hidden_message())
