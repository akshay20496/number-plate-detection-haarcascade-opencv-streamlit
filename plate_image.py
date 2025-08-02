import cv2

class Plate_Image:

    def __init__(self,image_path,cascade_file,max_width=600):
        self.image_path = image_path
        self.cascade_file = cascade_file
        self.max_width = max_width

    def detect_plate(self):
        # load the cascde classifier
        plate_cascade = cv2.CascadeClassifier(self.cascade_file)

        # read the image
        image = cv2.imread(self.image_path)

        # Resize image if it's too large
        height, width = image.shape[:2]
        if width > self.max_width:
            scale_ratio = self.max_width / width
            new_dim = (int(width * scale_ratio), int(height * scale_ratio))
            image = cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

        # convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        plates = plate_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

        # draw rectangle around the plates
        for (x, y, w, h) in plates:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,255), 3)

            cv2.putText(image, "Number Plate", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)

        # Save the annotated image
        output_path = "temp/annotated_image.jpg"
        cv2.imwrite(output_path, image)

        return image # return the image with detected plates

if __name__ == "__main__":
    image_path = "car_image.jpg"  # Change this to your input image path
    cascade_file = "haarcascade_russian_plate_number.xml"

    detector = Plate_Image(image_path, cascade_file)
    result_image = detector.detect_plate()

    # Display the result using matplotlib
    cv2.imshow("Detected Plate", result_image)
    cv2.waitKey(10000) # 10 seconds = 10000 milliseconds
    cv2.destroyAllWindows()

        