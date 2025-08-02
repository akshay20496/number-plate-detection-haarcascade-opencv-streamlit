
# video.py
import cv2
import os
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

class Plate_Video:
    def __init__(self, video_path, cascade_file):
        self.video_path = video_path
        self.cascade_file = cascade_file

    def detect_plate(self):
        plate_cascade = cv2.CascadeClassifier(self.cascade_file)
        if plate_cascade.empty():
            print("Error: Failed to load cascade classifier.")
            return None

        cam = cv2.VideoCapture(self.video_path)
        if not cam.isOpened():
            print("Error: Could not open video.")
            return None

        fps = cam.get(cv2.CAP_PROP_FPS)
        if fps == 0 or fps is None:
            fps = 30 # Default to 30 FPS if not available

        frames = []
        while True:
            ret, frame = cam.read()
            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            plates = plate_cascade.detectMultiScale(gray_frame, 1.1, 5)

            for (x, y, w, h) in plates:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
                cv2.putText(frame, "Number Plate", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

            frame = cv2.resize(frame, (640, 360))
            frames.append(frame)

        cam.release()

        output_path = os.path.join("temp", "output.mp4")
        self.save_video(frames, output_path, fps)

        return frames, output_path

    def save_video(self, frames, output_file, fps):
        if not frames:
            return None

        # Convert frames from BGR (OpenCV) to RGB (MoviePy)
        rgb_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]

        clip = ImageSequenceClip(rgb_frames, fps=fps)
        clip.write_videofile(output_file, codec='libx264', audio=False)

        return output_file


if __name__ == "__main__":
    video_path = "number_plate_video.mp4"  # Change this to your input video path
    cascade_file = "haarcascade_russian_plate_number.xml"

    detector = Plate_Video(video_path, cascade_file)
    frames,result_video_path = detector.detect_plate()

    if result_video_path:
        print("Video saved at:", result_video_path)

        # Optional: play result video
        cap = cv2.VideoCapture(result_video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Detected Plate Video", frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print("Detection failed.")