# AI-Canvas
✋ AI Virtual Painter (Finger Drawing using Computer Vision)

An AI-based Virtual Drawing Application that allows users to draw in the air using hand gestures, without touching the screen.
Built using Python, OpenCV, and MediaPipe, this project uses real-time hand landmark detection to create an interactive painting experience.

📌 Features

🎥 Real-time webcam-based hand tracking

✍️ Draw using index finger gestures

🎨 Color selection using on-screen toolbar

🧹 Eraser tool

🧼 Clear canvas gesture

🧠 Gesture-based mode switching (Draw / Select)

⚡ Smooth & responsive drawing

🧠 Project Concept

The system detects 21 hand landmarks using MediaPipe.
Based on finger positions, it determines:

Which fingers are raised

Which mode the user is in

Where to draw or what to select

All drawing is done on a virtual canvas, which is merged with the live video feed.

🛠️ Tech Stack
Technology	Purpose
Python	Core programming
OpenCV	Video processing & drawing
MediaPipe	Hand landmark detection
NumPy	Canvas & array operations
🖐️ Hand Landmarks Used
Landmark	Finger
4	Thumb tip
8	Index finger tip
12	Middle finger tip
16	Ring finger tip
20	Little finger tip
✨ Gesture Controls
✍️ Drawing Mode

Gesture: Index finger up

Action: Draw on canvas

🎨 Selection Mode

Gesture: Index + Middle finger up

Action: Select color / eraser from toolbar

🧹 Clear Canvas

Gesture: All fingers up

Action: Clears entire canvas

🎨 Toolbar Options

Pink

Blue

Green

Yellow

Eraser

Selection is done by placing the index finger over the toolbar.

📂 Project Structure
AI-Virtual-Painter/
│
├── main.py          # Main application file
├── README.md        # Project documentation
└── requirements.txt # Dependencies (optional)

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-virtual-painter.git
cd ai-virtual-painter

2️⃣ Install Dependencies
pip install opencv-python mediapipe numpy

3️⃣ Run the Project
python main.py

📸 Output

Live webcam feed

Hand landmarks displayed

Drawing appears smoothly in real time

No mouse or keyboard required
