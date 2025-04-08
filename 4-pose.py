import cv2 as cv
import mediapipe as mp
import numpy as np

width = 1280
height = 720

# Initialize Mediapipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radian = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radian * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

# Webcam
camera = cv.VideoCapture(0)
camera.set(cv.CAP_PROP_FRAME_WIDTH, width)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, height)

# Initialize counters and curl statuses for both arms
counter_right = 0
counter_left = 0
in_curl_right = False  # To check if we are in a curl motion for the right arm
in_curl_left = False   # To check if we are in a curl motion for the left arm

while camera.isOpened():
    success, frame = camera.read()
    if not success:
        break

    frame = cv.flip(frame, 1)
    rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Right arm landmarks
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        # Left arm landmarks
        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                      landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

        # Calculate angles for both arms
        angle_right = calculate_angle(right_shoulder, right_elbow, right_wrist)
        angle_left = calculate_angle(left_shoulder, left_elbow, left_wrist)

        # Visualize angles for both arms
        location_right = tuple(np.multiply(right_elbow, [width, height]).astype(int))
        location_left = tuple(np.multiply(left_elbow, [width, height]).astype(int))
        color = (0, 255, 0) # Green
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2
        cv.putText(frame, str(int(angle_right)), location_right, font, font_scale, color, font_thickness)
        cv.putText(frame, str(int(angle_left)), location_left, font, font_scale, color, font_thickness)

        # Counter logic for right arm
        if angle_right < 30:  # If angle is less than 30, it means the arm is curled
            if not in_curl_right:  # If we're not already counting a curl
                counter_right += 1  # Increment counter (curl completed)
                in_curl_right = True  # Mark that we are in the curl position
        else:  # Reset when the arm is extended
            in_curl_right = False

        # Counter logic for left arm
        if angle_left < 30:  # If angle is less than 30, it means the arm is curled
            if not in_curl_left:  # If we're not already counting a curl
                counter_left += 1  # Increment counter (curl completed)
                in_curl_left = True  # Mark that we are in the curl position
        else:  # Reset when the arm is extended
            in_curl_left = False

        # Draw landmarks on frame
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the curl counter for both arms
    cv.rectangle(frame, (0, 0), (600, 70), (0, 255, 0), -1)  # Background box
    cv.putText(frame, f'Right Arm: {counter_right}', (50, 30),
                cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Right arm counter
    cv.putText(frame, f'Left Arm: {counter_left}', (50, 60),
                cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)  # Left arm counter

    cv.imshow('Webcam', frame)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()
