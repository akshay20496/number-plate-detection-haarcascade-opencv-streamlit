import streamlit as st
import cv2
import time
import os
from dotenv import load_dotenv
from plate_image import Plate_Image
from plate_video import Plate_Video

load_dotenv()
cascade_file = os.getenv("cascade_file")

st.title("Number Plate Detection App")
    
# File uploader for image or video
uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4"])

if uploaded_file is not None:
    # Ensure temp folder exists
    os.makedirs("temp", exist_ok=True)

    # Save the uploaded file to a temporary location
    temp_file_path = os.path.join("temp", uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Check if the uploaded file is an image or video
    # IMAGE PROCESSING
    if uploaded_file.type.startswith("image/"):
        detector = Plate_Image(temp_file_path, cascade_file)
        result_image = detector.detect_plate()
        rgb_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
        if rgb_image is not None:
            st.image(rgb_image, caption="Detected Number Plate", use_container_width=True)
        else:
            st.error("Could not process the image.")

        # Remove uploaded image after processing
        os.remove(temp_file_path)
    
    # VIDEO PROCESSING
    elif uploaded_file.type.startswith("video/"):
        st.info("Processing video, please wait...")
        detector = Plate_Video(temp_file_path, cascade_file)
        frames, video_path = detector.detect_plate()

        if frames:
            st.success("Video processed successfully!")

            # Display video
            if os.path.exists(video_path):
                st.video(video_path)
                with open(video_path, 'rb') as f:
                    st.download_button("Download Video", f, file_name="detected_output.mp4")

            # Show frame preview (optional)
            st.info("Previewing frames:")
            for idx, frame in enumerate(frames[::100]):  # Show every 100th frame for performance
                st.image(frame, channels="BGR", caption=f"Frame {idx+1}")
                time.sleep(0.03)
        else:
            st.error("No frames found or video could not be processed.")

        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)