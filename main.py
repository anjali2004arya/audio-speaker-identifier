import os
import torchaudio
from dotenv import load_dotenv

from transcriber import transcribe_audio
from diarizer import diarize_audio
from speaker_identifier import get_known_embeddings, match_speaker

def extract_segment(audio_path, start, end, output_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    start_frame, end_frame = int(start * sample_rate), int(end * sample_rate)
    segment = waveform[:, start_frame:end_frame]
    torchaudio.save(output_path, segment, sample_rate)

def main():
    # Load Hugging Face token from .env file
    load_dotenv()
    hf_token = os.getenv("HF_AUTH_TOKEN")

    if not hf_token:
        print(" HF_AUTH_TOKEN not found in environment. Please check your .env file.")
        return

    audio_path = "test_audio.wav"
    known_dir = "known_speakers"

    print(" Transcribing audio...")
    transcript = transcribe_audio(audio_path)

    print("Performing speaker diarization...")
    diarization = diarize_audio(audio_path, hf_token)

    if diarization is None:
        print(" Diarization failed. Ensure your Hugging Face token is valid and you have access to the model.")
        return

    print(" Generating known speaker embeddings...")
    known_embeddings = get_known_embeddings(known_dir)

    print("\n=== Speaker Segments ===")
    for turn, _, _ in diarization.itertracks(yield_label=True):
        segment_path = f"temp_{int(turn.start*100)}_{int(turn.end*100)}.wav"
        extract_segment(audio_path, turn.start, turn.end, segment_path)
        speaker = match_speaker(segment_path, known_embeddings)
        print(f"{speaker}: {turn.start:.2f}s - {turn.end:.2f}s")
        os.remove(segment_path)

    print("\n=== Transcript ===")
    print(transcript)

if __name__ == "__main__":
    main()
