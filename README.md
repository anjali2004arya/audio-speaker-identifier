# 🎙️ Audio Speaker Identifier

This project is an audio processing pipeline that performs:

- ✅ Automatic speech transcription
- Speaker diarization using [pyannote-audio](https://github.com/pyannote/pyannote-audio)
- Speaker identification by comparing segments to known speaker embeddings 

---

## 🔧 Features

- Transcribes any `.wav` audio file into text
- Splits audio into segments per speaker
- Matches speakers to a known database using audio embeddings
- Automatically handles temporary audio segmentation
- Includes error handling and secure token management via `.env` 

---

## 📁 Project Structure

```

audio-speaker-identifier/
├── main.py                  # Main entry point
├── diarizer.py              # Handles speaker diarization
├── transcriber.py           # Performs speech-to-text transcription
├── speaker_identifier.py    # Matches speakers using embeddings
├── known_speakers/          # Directory containing known speaker audio samples
├── test_audio.wav           # Sample audio file for testing
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```


---

## 🧪 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/anjali2004arya/audio-speaker-identifier.git
cd audio-speaker-identifier
```


### 2. Create and Activate Conda Environment

```bash
conda create -n speaker-id python=3.8
conda activate speaker-id
```


### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Hugging Face API token:

```bash
HUGGINGFACE_TOKEN=your_huggingface_token_here
```


*Note: Ensure you have access to the necessary models on Hugging Face.*

---

## 🚀 Usage

To process an audio file and identify speakers

```bash
python main.py
```


The script will:

1. Perform speaker diarization on `test_audio.wav`.
2. Transcribe each speaker segment.
3. Compare segments to known speakers in the `known_speakers/` directory.
4. Output the transcription with identified speakers.

---

## 🗣️ Adding Known Speakers

To add a new known speaker:

1. Place a `.wav` file of the speaker's voice in the `known_speakers/` directory.
2. Name the file appropriately (e.g., `alice.wav`).

The system will use these samples to match speakers in the input audio.

---
 