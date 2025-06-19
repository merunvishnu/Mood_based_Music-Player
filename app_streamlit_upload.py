import streamlit as st
from PIL import Image
import numpy as np
import random
import webbrowser
from deepface import DeepFace
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Spotify API setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-playback-state,user-read-currently-playing"
))

# Map detected emotion to Tamil song themes
emotion_to_tamil_query = {
    "happy": "tamil happy",
    "sad": "tamil sad",
    "angry": "tamil kuthu",
    "neutral": "tamil chill",
    "surprise": "tamil melody",
    "fear": "tamil instrumental",
    "disgust": "tamil retro"
}

# App UI
st.title("📸 Tamil Mood Music Player")
st.write("Upload a selfie and we'll detect your mood to recommend a Tamil song 🎶")

uploaded_file = st.file_uploader("Upload your face image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption='Uploaded Image', use_column_width=True)

        img_np = np.array(image)

        st.write("🔍 Detecting emotion...")
        result = DeepFace.analyze(img_np, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        st.success(f"🧠 Detected Emotion: `{emotion}`")

        # Get query based on emotion
        query = emotion_to_tamil_query.get(emotion.lower(), "tamil songs")
        st.write(f"🎯 Finding Tamil songs for: **{query}**")

        # Search Spotify
        results = sp.search(q=query, type="track", limit=10)
        tracks = results['tracks']['items']

        if not tracks:
            st.warning("No songs found for this mood.")
        else:
            track = random.choice(tracks)
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']

            st.success(f"🎵 Now playing: **{name}** by *{artist}*")
            st.markdown(f"[▶️ Open on Spotify]({url})", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
