import cv2
from pyfeat import FacialExpressionDetector


def main():
    # Initialize the PyFEAT emotion detector
    detector = FacialExpressionDetector()

    # Open a connection to the webcam (usually 0 for the default camera)
    cap = cv2.VideoCapture(0)

    frame_count = 0  # Counter for frames

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop if there's an issue with the webcam

        frame_count += 1

        # Detect emotions for every 30th frame
        if frame_count % 30 == 0:
            emotions = detector.detect_emotions(frame)
            print("Emotions detected:", emotions)

        # Display the frame with detected emotions
        cv2.imshow('Emotion Detection', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
