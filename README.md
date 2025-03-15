# WorkplaceSafetyCompliance-AI
🚀 PPE Detection System with YOLOv8
     by GOTTK5
__________________________________________________________________________________________________
📌 Overview
This project is a real-time PPE (Personal Protective Equipment) Detection System using YOLOv8. It detects whether workers are wearing essential safety gear (Helmet, Goggles, Gloves, Boots, and Vest) from various video sources, including:
Webcam (Live Feed)
YouTube Video Streams
CCTV/RTSP Streams
It features encrypted code protection to prevent unauthorized use and copying.⚡
_________________________________________________________________
✨ Features
✅ Real-time PPE Detection (Helmet, Goggles, Gloves, Boots, Vest)
✅ Multi-Source Video Support (Webcam, YouTube, CCTV)
✅ Smart Alert System (Triggers alerts after 10s if PPE is missing)
✅ Encrypted Code Protection (To prevent unauthorized copying)
✅ Non-Blocking Alerts (Pop-up & Beep Sound)
✅ Customizable & Expandable
__________________________________________________________________________________________________
🔧 Installation & Setup
1️⃣ Install Dependencies
Ensure Python and pip are installed, then run:
pip install ultralytics opencv-python numpy pillow yt-dlp
2️⃣ Clone This Repository

git clone <https://github.com/GOTTK5/WorkplaceSafetyCompliance-AI.git>
cd WORKPLACE-SAFETY-COMPLIANCE

3️⃣ Run the Script
1. For IMAGE PPE DETECTION :: ( detects PPE in an image without any alert message)
1_imgdet.py                      
2.🎥 For BASIC YouTube Stream PPE DETECTION ::( detects PPE from a youtube video without any alert message)
Edit VIDEO_SOURCE in the script:
VIDEO_SOURCE = "https://youtu.be/YOUR_VIDEO_LINK" 
or simply run
Run:
2_basicyt.py                      
3.FOR WEBCAMERA ONLY PPE DETECTION :: (no alert only detection)
3_basicweb.py                 
4.FOR GOGGLES DETECTION AND ALERT::( only gives alert for goggles. This is for testing if you only have goggles or specs not for  other PPE’s )
4_goggalert.py                 
5.FOR WEBCAM DETECTION ALONG WITH ALERT::( PEE detection along with alert on web camera )
5_webcam.py                   
6.📡 FOR CCTV RTSP STREAM ALONG WITH ALERT :: ( For CCTV and Yt Videos along with alert  )
Edit VIDEO_SOURCE:
VIDEO_SOURCE = "rtsp://username:password@IP:PORT/stream"
Run:
6_ytandcamera.py           
_________________________________________________________________
🛠 How It Works
1️⃣ The YOLOv8 model detects PPE in real-time.
2️⃣ If a required PPE is not detected for 10 seconds, an alert triggers (Beep + Pop-up).
3️⃣ Encrypted code protection prevents unauthorized copying.
__________________________________________________________________________________________________
Dataset Information
Special thanks to Roboflow for their toolkit.
__________________________________________________________________________________________________
📈 Model Training Details
The YOLOv8 model is trained for 100 epochs, which may lead to variations in detection accuracy. 
*Further updates and improvements will be made to enhance system performance.
__________________________________________________________________________________________________
🔒 License & Security
This project includes code encryption to prevent misuse. If unauthorized usage is detected, it will display:
Copied Code Detected! GOTTK5 @copied code of KRUPPK5
Use this project only for learning and research purposes.
_________________________________________________________________________________________________
🤖 Future Enhancements
🔹 Add email notifications for violations
🔹 Integrate AI-based PPE compliance tracking
🔹 Improve detection accuracy with fine-tuned models
__________________________________________________________________________________________________
🚀 Developed & Secured by GOTTK5
      gottkrupp@gmail.com
