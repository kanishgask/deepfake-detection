import cv2
import random

def extract_frames(video):

    cap=cv2.VideoCapture(video)

    frames=[]

    while cap.isOpened():

        ret,frame=cap.read()

        if not ret:
            break

        frame=cv2.resize(
            frame,
            (128,128)
        )

        frames.append(frame)

        if len(frames)==20:
            break

    cap.release()

    return frames


def predict_fake(video_path):

    frames=extract_frames(video_path)

    # Placeholder prediction
    # Replace with trained model later

    score=random.uniform(0,1)

    if score>0.5:
        return "Deepfake Detected"

    else:
        return "Authentic Video"
