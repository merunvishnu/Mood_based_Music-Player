import cv2
import os
import random
from deepface import DeepFace
from playsound import playsound

emotion_to_music = {
    "happy": "songs/happy",
    "sad": "songs/sad",
    "angry": "songs/angry",
    "neutral": "songs/neutral",
    "surprise": "songs/surprise"
}

def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture image from webcam.")
        return None
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print(f"Detected Emotion: {emotion}")
        return emotion
    except Exception as e:
        print(f"Error: {e}")
        return None

def play_music(emotion):
    music_dir = emotion_to_music.get(emotion.lower(), "songs/neutral")
    if not os.path.exists(music_dir):
        print("No music found.")
        return
    songs = os.listdir(music_dir)
    if not songs:
        print("No songs in folder.")
        return
    song = random.choice(songs)
    print(f"Playing: {song}")
    playsound(os.path.join(music_dir, song))

if __name__ == "__main__":
    emotion = detect_emotion()
    if emotion:
        play_music(emotion)
