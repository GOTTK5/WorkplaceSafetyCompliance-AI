

import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
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

# Load the image
image_path = "TEST.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("⚠️ Error: Couldn't load the image.")
    exit()

# Run YOLO detection
results = model(image)
annotated_image = results[0].plot()
# Convert BGR to RGB for Matplotlib
img_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

# Print watermark in console
print(Obfuscated._hidden_message())

# Display the image with Matplotlib
plt.imshow(img_rgb)
plt.title(Obfuscated._hidden_message() + " - PPE Detection")
plt.axis("off")
plt.show()

















