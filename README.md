# Number Plate Detection using Haar Cascade, OpenCV & Streamlit

This project demonstrates automatic vehicle number plate detection using OpenCV's Haar Cascade classifier. A simple and interactive Streamlit web interface is included to visualize the detection process in real-time or on uploaded videos and images.

---

## 🚀 Features

- 📸 Detects number plates in images, or video files
- 🧠 Uses pre-trained Haar Cascade model (`haarcascade_russian_plate_number.xml`)
- 🎞️ Supports video processing using `moviepy`
- 🖼️ Draws bounding boxes around detected plates
- 🧪 Displays sample output files in `temp/` folder
- 🌐 Simple and fast Streamlit interface for user interaction

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- Streamlit
- MoviePy
- Haar Cascade Classifier

---

## 📁 Project Structure

├── haarcascade_russian_plate_number.xml # Pre-trained detection model
├── temp/
│ ├── annotation_image.jpg # Output: image with detected plate
│ └── output.mp4 # Output: processed video
├── car_image.jpg # Sample input image
├── number_plate_video.mp4 # Sample input video
├── num_plate_detection_app.py # Main Streamlit app
├── plate_image.py # Detection logic for images
├── plate_video.py # Detection logic for videos
├── requirements.txt # Python dependencies
└── README.md # This file


---

## ⚙️ Getting Started

**Clone the Repository**

git clone https://github.com/akshay20496/number-plate-detection-haarcascade-opencv-streamlit.git
cd number-plate-detection-haarcascade-opencv-streamlit

📦 **Install Dependencies:**

pip install -r requirements.txt

Contents of requirements.txt:

  - opencv-python

  - streamlit

  - moviepy

**Launch the App**

python -m streamlit run num_plate_detection_app.py

🧪 **Sample Inputs & Outputs**

🎯 **Inputs:**

    - car_image.jpg: A sample image containing a car with a visible number plate.

    - number_plate_video.mp4: A short video showing a car for testing plate detection.

✅ **Outputs (generated in temp/):**

    - annotation_image.jpg: Annotated image showing detected plate.

    - output.mp4: Video with bounding boxes drawn over detected plates.

These help users quickly understand what the detection output looks like.

📚 **Script Overview**
  - plate_image.py: Handles detection logic for single images.

  - plate_video.py: Processes each frame in a video and performs detection.

  - num_plate_detection_app.py: Streamlit UI to interact with both.

🙌 **Acknowledgments**

  - OpenCV for computer vision tools and Haar Cascades

  - Streamlit for interactive web app

  - MoviePy for video editing

📝 **License**

This project is licensed under the MIT License.

✍️ **Author**

**Akshay Ghatage**
🔗 [GitHub](https://github.com/akshay20496)

Happy to help!
