from pyannote.audio import Pipeline
import os

def diarize_audio(audio_path, hf_token):
    try:
        pipeline = Pipeline.from_pretrained(
            "pyannote/speaker-diarization-3.1",
            use_auth_token=hf_token
        )
        diarization = pipeline(audio_path)
        return diarization
    except Exception as e:
        print(f" Diarization error: {e}")
        print(" Ensure your Hugging Face token is valid and you have accepted model conditions at:")
        print("   https://huggingface.co/pyannote/speaker-diarization-3.1")
        return None
