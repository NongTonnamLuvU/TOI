from flask import Flask, render_template, Response
import cv2 as cv
import numpy as np
import mediapipe as mp
import math

app = Flask(__name__)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


def generate_frame():

    camera = cv.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break

        frame = cv.flip(frame, 1)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)


        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                landmarks = hand_landmarks.landmark
                height , width , _ = frame.shape
                thumb = (int(landmarks[4].x * width), int (landmarks[4].y * height))
                index = (int(landmarks[8].x * width), int (landmarks[8].y * height))

                distance = int(math.dist(thumb, index))
                radius = min(distance * 2 , 300)

                cv.circle(frame, thumb, radius, (255, 0 ,0),-1)

        _, buffer = cv.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


    camera.release()


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/video_feed")
def video():
    return Response(generate_frame(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/profile/<name>")
def user_profile(name): 
    return render_template("profile.html", username=name)

@app.route("/contract")
def contract(): 
    return render_template("contract.html")

if __name__ == "__main__":
    app.run(debug=True)
