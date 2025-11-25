import cv2 as cv
import mediapipe as mp

# Load the image
img = cv.imread('BSDS_376001.jpg')

# Check if image is loaded correctly
if img is None:
    print("Error: Image not loaded properly.")
else:
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    # Initialize face detection
    face_detection = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)

    # Convert the image to RGB format (MediaPipe expects RGB, not BGR)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    # Wrap the image in a MediaPipe ImageFrame
    img_frame = mp.ImageFrame(img_rgb)

    # Process the image with MediaPipe face detection
    res = face_detection.process(img_frame)

    if not res.detections:
        print('No face detected')
    else:
        # Draw the face detection results on the image
        for detection in res.detections:
            mp_drawing.draw_detection(img, detection)

        # Show the result
        cv.imshow('Face Detection', img)

    # Wait for a key press and close the window
    cv.waitKey(0)
    cv.destroyAllWindows()
