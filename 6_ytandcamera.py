


import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox  # ✅ Import messagebox separately   GOTTK5
import winsound  # For beep alerts
import threading  # For non-blocking pop-ups  GOTTK5
import base64
import os
import time
import yt_dlp

# Store the encrypted watermark in a hidden environment variable
if not os.environ.get("WATERMARK"):
    os.environ["WATERMARK"] = base64.b64encode("Original YOLOv8 PPE Detection Code by [GOTTK5]".encode()).decode()

class Obfuscated:
    @staticmethod
    def _hidden_message():
        encoded_message = os.environ.get("WATERMARK")
        return base64.b64decode(encoded_message).decode() if encoded_message else "Copied Code Detected! GOTTK5 @copied code of GOTTK5"

# Load YOLOv8 model
model = YOLO("best.pt")  # Ensure best.pt is in the same folder

# Define the video source (webcam, YouTube link, or RTSP stream)
VIDEO_SOURCE = 0  # For webcam
# VIDEO_SOURCE = "https://youtu.be/L0Yy46xLUCw?feature=shared"  # For YouTube
# VIDEO_SOURCE = "rtsp://username:password@<IP_ADDRESS>:<PORT>/stream"  # For CCTV

# Initialize Tkinter window
root = tk.Tk()
root.title(Obfuscated._hidden_message())

# Create a label for video display
video_label = tk.Label(root)
video_label.pack()

# Handle YouTube stream
if "youtube.com" in str(VIDEO_SOURCE) or "youtu.be" in str(VIDEO_SOURCE):
    ydl_opts = {"format": "best[ext=mp4]"}  # Get best quality MP4 stream
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(VIDEO_SOURCE, download=False)
        video_url = info_dict["url"]
    cap = cv2.VideoCapture(video_url)
else:
    cap = cv2.VideoCapture(VIDEO_SOURCE)

# Track last alert time
last_alert_time = 0
ALERT_INTERVAL = 10  # Minimum time between alerts (in seconds)

# Function to show pop-up alert without stopping video
def show_alert(message):
    def popup():
        alert = tk.Toplevel(root)
        alert.title("Safety Alert")
        label = tk.Label(alert, text=message, font=("Arial", 14), fg="red")
        label.pack(padx=20, pady=10)
        alert.after(2000, alert.destroy)  # Close pop-up after 2 sec

    threading.Thread(target=popup).start()  # Run pop-up in a new thread

# Function to update frames and check for PPE violations
def update_frame():
    global last_alert_time

    ret, frame = cap.read()
    if not ret:
        return

    # Run YOLOv8 detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Convert frame for Tkinter display
    img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    # Update Tkinter window
    video_label.img = img
    video_label.config(image=img)

    # Detect PPE items
    detected_ppe = set()

    for result in results:
        for box in result.boxes:
            cls = result.names[int(box.cls[0])]  # Get class name
            detected_ppe.add(cls)  # Store detected PPE

    # Alert only if PPE items are missing and after the alert interval
    required_ppe = {"Helmet", "Goggles", "Glove", "Boot", "Vest"}
    missing_ppe = required_ppe - detected_ppe

    if missing_ppe and (time.time() - last_alert_time > ALERT_INTERVAL):
        alert_message = f'⚠️ ALERT! Missing PPE: {', '.join(missing_ppe)} - KRUPPK5'
        last_alert_time = time.time()
        print(alert_message)  # Console alert
        winsound.Beep(1000, 300)  # Beep 1 (short beep)
        winsound.Beep(1000, 300)  # Beep 2 (short beep)
        show_alert(alert_message)  # Non-blocking pop-up

    root.after(30, update_frame)  # Faster video update for smoother display

# Run the update function
update_frame()
root.mainloop()

# Release the video source when the window is closed
cap.release()

# Print watermark at the end
print(Obfuscated._hidden_message())
