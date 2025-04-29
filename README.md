# 🎙️ Speaker Identification & Transcription System

This project is an **audio processing pipeline** that performs:

- ✅ **Automatic speech transcription**
- 🧠 **Speaker diarization** using [pyannote-audio](https://huggingface.co/pyannote/speaker-diarization-3.1)
- 🧍 **Speaker identification** by comparing segments to known speaker embeddings

---

## 🚀 Features

- Transcribes any audio file (`.wav`) into text
- Splits audio into segments per speaker
- Matches speakers to a known database using audio embeddings
- Automatically handles temporary audio segmentation
- Includes error handling and secure token management via `.env`

---

## 🗂️ Project Structure

```
📁 project-root/
├── main.py                  # Main entry point
├── diarizer.py              # Handles speaker diarization
├── transcriber.py           # Transcribes audio (requires Whisper or other tool)
├── speaker_identifier.py    # Compares speakers to known database
├── known_speakers/          # Directory with known speaker audio clips
├── test_audio.wav           # Input audio file to analyze
├── .env                     # Contains HF_AUTH_TOKEN
└── requirements.txt         # Python dependencies
```

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/speaker-identification.git
cd speaker-identification
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Hugging Face Token Setup

### 1. Get a token from: https://huggingface.co/settings/tokens

### 2. Accept access to the model:
- Visit: https://huggingface.co/pyannote/speaker-diarization-3.1
- Click **"Access repository"** or **agree to terms**

### 3. Create a `.env` file in the project root:

```
HF_AUTH_TOKEN=hf_your_actual_token_here
```

---

## ▶️ Usage

```bash
python main.py
```

Output:
- Transcribed text
- List of speaker-labeled segments with start and end times

---

## 📁 Known Speakers

Add `.wav` files for each known speaker in the `known_speakers/` folder.  
File names should be descriptive (e.g., `alice.wav`, `bob.wav`).  
The system will extract embeddings and use them for matching.

---

## 📦 Requirements

- Python 3.8+
- `torch`, `torchaudio`
- `pyannote.audio`
- `openai-whisper` or other ASR for `transcriber.py`
- `python-dotenv`

---

## 📌 Notes

- This project is designed to work with mono WAV files. Use tools like `ffmpeg` to convert if needed.
- Transcription and diarization are computationally intensive and may require a GPU for large files.
- Temporary audio segments are automatically deleted after processing.


---

## ✨ Acknowledgements

- [Hugging Face](https://huggingface.co/)
- [pyannote-audio](https://github.com/pyannote/pyannote-audio)
- [Whisper by OpenAI](https://github.com/openai/whisper)

