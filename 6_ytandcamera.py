


import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox  #    GOTTK5
import winsound  
import threading  #  GOTTK5
import base64
import os
import time
import yt_dlp

 
if not os.environ.get("WATERMARK"):
    os.environ["WATERMARK"] = base64.b64encode("Original YOLOv8 PPE Detection Code by [GOTTK5]".encode()).decode()

class Obfuscated:
    @staticmethod
    def _hidden_message():
        encoded_message = os.environ.get("WATERMARK")
        return base64.b64decode(encoded_message).decode() if encoded_message else "Copied Code Detected! GOTTK5 @copied code of GOTTK5"

model = YOLO("best.pt") 


VIDEO_SOURCE = 0  
# VIDEO_SOURCE = "https://youtu.be/L0Yy46xLUCw?feature=shared"  # For YouTube
# VIDEO_SOURCE = "rtsp://username:password@<IP_ADDRESS>:<PORT>/stream"  # For CCTV


root = tk.Tk()
root.title(Obfuscated._hidden_message())


video_label = tk.Label(root)
video_label.pack()


if "youtube.com" in str(VIDEO_SOURCE) or "youtu.be" in str(VIDEO_SOURCE):
    ydl_opts = {"format": "best[ext=mp4]"}  
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(VIDEO_SOURCE, download=False)
        video_url = info_dict["url"]
    cap = cv2.VideoCapture(video_url)
else:
    cap = cv2.VideoCapture(VIDEO_SOURCE)


last_alert_time = 0
ALERT_INTERVAL = 10  # Minimum time between alerts (in seconds)

def show_alert(message):
    def popup():
        alert = tk.Toplevel(root)
        alert.title("Safety Alert")
        label = tk.Label(alert, text=message, font=("Arial", 14), fg="red")
        label.pack(padx=20, pady=10)
        alert.after(2000, alert.destroy)  
    threading.Thread(target=popup).start() 

def update_frame():
    global last_alert_time

    ret, frame = cap.read()
    if not ret:
        return

    results = model(frame)
    annotated_frame = results[0].plot()

    
    img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

  
    video_label.img = img
    video_label.config(image=img)

    
    detected_ppe = set()

    for result in results:
        for box in result.boxes:
            cls = result.names[int(box.cls[0])] 
            detected_ppe.add(cls)  

    
    required_ppe = {"Helmet", "Goggles", "Glove", "Boot", "Vest"}
    missing_ppe = required_ppe - detected_ppe

    if missing_ppe and (time.time() - last_alert_time > ALERT_INTERVAL):
        alert_message = f'⚠️ ALERT! Missing PPE: {', '.join(missing_ppe)} - KRUPPK5'
        last_alert_time = time.time()
        print(alert_message) 
        winsound.Beep(1000, 300)  
        winsound.Beep(1000, 300)  
        show_alert(alert_message) 
    root.after(30, update_frame) 


update_frame()
root.mainloop()

# Release the video source when the window is closed
cap.release()

# Print watermark at the end
print(Obfuscated._hidden_message())
