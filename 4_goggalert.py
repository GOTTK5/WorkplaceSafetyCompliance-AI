

import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox 
import winsound  
import threading  
import base64
import os
import time


if not os.environ.get("WATERMARK"):
    os.environ["WATERMARK"] = base64.b64encode("Original YOLOv8 PPE Detection Code by [GOTTK5]".encode()).decode()

class Obfuscated:
    @staticmethod
    def _hidden_message():
        encoded_message = os.environ.get("WATERMARK")
        return base64.b64decode(encoded_message).decode() if encoded_message else "Copied Code Detected! GOTTK5 @copied code of GOTTK5"


model = YOLO("best.pt")  


root = tk.Tk()
root.title(Obfuscated._hidden_message())


video_label = tk.Label(root)
video_label.pack()


cap = cv2.VideoCapture(0)


last_alert_time = 0
ALERT_INTERVAL = 15  


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

    
    if "Goggles" not in detected_ppe and (time.time() - last_alert_time > ALERT_INTERVAL):
        last_alert_time = time.time()
        print("🚨 ALERT! Goggles missing!")  
        winsound.Beep(1000, 300)  
        winsound.Beep(1000, 300) 
        show_alert("⚠️ ALERT! Goggles not detected - KRUPPK5")  

    root.after(30, update_frame)  


update_frame()
root.mainloop()


cap.release()

print(Obfuscated._hidden_message())
