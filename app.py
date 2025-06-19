import cv2
import random
import webbrowser
import os
from deepface import DeepFace
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load credentials from .env file
load_dotenv()

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-playback-state,user-read-currently-playing"
))

# Emotion to genre mapping
emotion_to_genre = {
    "happy": "pop",
    "sad": "acoustic",
    "angry": "metal",
    "neutral": "chill",
    "surprise": "dance"
}

def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Webcam not detected.")
        return None

    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        print(f"Detected Emotion: {emotion}")
        return emotion
    except Exception as e:
        print(f"Emotion detection error: {e}")
        return None

def play_spotify_song(emotion):
    genre = emotion_to_genre.get(emotion.lower(), "pop")
    results = sp.search(q=f"genre:{genre}", type="track", limit=10)
    track = random.choice(results['tracks']['items'])
    url = track['external_urls']['spotify']
    print(f"Now playing: {track['name']} by {track['artists'][0]['name']}")
    webbrowser.open(url)

if __name__ == "__main__":
    emotion = detect_emotion()
    if emotion:
        play_spotify_song(emotion)
