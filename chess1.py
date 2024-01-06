import cv2
import dlib

# Load the pre-trained face and shape predictor models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
shape_predictor = dlib.shape_predictor('path/to/shape_predictor_68_face_landmarks.dat')

# Function to detect faces, eyes, and draw facial landmarks from webcam feed
def detect_faces_eyes_landmarks():
    # Open a connection to the webcam (usually 0 or 1, depending on your setup)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Detect eyes within the detected face region
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

            # Detect facial landmarks
            dlib_rect = dlib.rectangle(x, y, x + w, y + h)
            landmarks = shape_predictor(gray, dlib_rect)

            for i in range(68):
                x_landmark = landmarks.part(i).x
                y_landmark = landmarks.part(i).y
                cv2.circle(frame, (x_landmark, y_landmark), 2, (0, 255, 255), -1)

        # Display the resulting frame
        cv2.imshow('Face, Eye, and Landmark Detection', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run the webcam face, eye, and landmark detection
detect_faces_eyes_landmarks()
