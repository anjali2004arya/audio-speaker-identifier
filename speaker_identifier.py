import os
import torchaudio
from scipy.spatial.distance import cosine
from speechbrain.inference.speaker import EncoderClassifier

classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb")

def get_embedding(path):
    signal, fs = torchaudio.load(path)
    embedding = classifier.encode_batch(signal).squeeze().detach().numpy()
    return embedding

def get_known_embeddings(known_dir):
    embeddings = {}
    for file in os.listdir(known_dir):
        if file.endswith(".wav"):
            name = os.path.splitext(file)[0]
            embeddings[name] = get_embedding(os.path.join(known_dir, file))
    return embeddings

def match_speaker(segment_audio_path, known_embeddings):
    segment_embedding = get_embedding(segment_audio_path)
    min_distance = float("inf")
    best_match = "Unknown"
    for name, embedding in known_embeddings.items():
        dist = cosine(segment_embedding, embedding)
        if dist < min_distance:
            min_distance = dist
            best_match = name
    return best_match
