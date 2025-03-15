

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import yt_dlp  # To fetch YouTube video stream
import pafy  # For video processing
import base64
import os

# Store the encrypted watermark in a hidden environment variable
if not os.environ.get("WATERMARK"):
    os.environ["WATERMARK"] = base64.b64encode("Original YOLOv8 PPE Detection Code by [GOTTK5]".encode()).decode()

class Obfuscated:
    @staticmethod
    def _hidden_message():
        encoded_message = os.environ.get("WATERMARK")
        return base64.b64decode(encoded_message).decode() if encoded_message else "Copied Code Detected! GOTTK5 "

# Load the trained YOLO model
model = YOLO("best.pt")

# YouTube Video URL
video_url = "https://youtu.be/OPs4MQOlZAQ?feature=shared"  # Replace with actual video link

# Get video stream
ydl_opts = {"format": "best"}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    video_url = info_dict["url"]

cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print("⚠️ Error: Couldn't access the YouTube video.")
    exit()

# Print watermark in console
print(Obfuscated._hidden_message())

# Set frame rate to increase video speed
frame_rate = 2  # Process every 2nd frame to speed up
frame_count = 0

# Create a figure for Matplotlib
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
plt.gcf().canvas.manager.set_window_title(Obfuscated._hidden_message())

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Error: Couldn't fetch frame from YouTube video.")
        break

    frame_count += 1
    
    # Process only every nth frame to increase speed
    if frame_count % frame_rate != 0:
        continue

    # Run YOLO detection
    results = model(frame)
    annotated_frame = results[0].plot()

    # Convert BGR to RGB for Matplotlib
    img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

    # Display the frame using Matplotlib
    ax.clear()
    ax.imshow(img)
    ax.set_title(Obfuscated._hidden_message())
    ax.axis("off")
    plt.pause(0.01)  # Small delay for refreshing frame

    # **Check if window is closed**
    if not plt.fignum_exists(fig.number):
        print("🚀 Video Closed! Exiting...")
        break

# Release resources
cap.release()
plt.close()

# Print watermark at the end
print(Obfuscated._hidden_message())
