# 🎵 MoodTunes - AI-Based Music Player Using Emotion Detection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

🎶 MoodTunes is a smart music player that detects your mood using facial emotion recognition and plays songs that match your current emotion!

## 👁️ How It Works

- Captures your face using webcam.
- Uses AI (`DeepFace`) to detect emotion.
- Plays a song from a folder mapped to that emotion.

## 📂 Folder Structure

```
mood_music_player/
├── app.py              # Main Python Script (CLI)
├── app_gui.py          # Optional Streamlit GUI
├── requirements.txt    # Python dependencies
├── README.md
└── songs/
    ├── happy/
    ├── sad/
    ├── angry/
    ├── neutral/
    └── surprise/
```

## 🚀 Run the Project

### ⏯️ CLI Mode

```bash
pip install -r requirements.txt
python app.py
```

### 🌐 GUI Mode (Streamlit)

```bash
streamlit run app_gui.py
```

## 🎧 Add Songs

Place `.mp3` or `.wav` files in their respective folders inside `/songs`.

## 🛠️ Dependencies

- Python 3.8+
- OpenCV
- DeepFace
- Playsound
- Streamlit (optional)

## 📝 License

MIT License

---

Made with ❤️ by [YourName]
