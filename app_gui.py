import streamlit as st
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
        return None
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except:
        return None

def play_music(emotion):
    music_dir = emotion_to_music.get(emotion.lower(), "songs/neutral")
    songs = os.listdir(music_dir)
    song = random.choice(songs)
    playsound(os.path.join(music_dir, song))

st.title("🎶 Mood-Based Music Player")

if st.button("Detect Mood & Play Music"):
    st.write("Capturing and analyzing mood...")
    emotion = detect_emotion()
    if emotion:
        st.success(f"Emotion: {emotion}")
        st.write("Playing music for your mood...")
        play_music(emotion)
    else:
        st.error("Failed to detect emotion.")
