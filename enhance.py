import torch
import librosa
import soundfile as sf
import numpy as np
from demucs.pretrained import get_model
from demucs.apply import apply_model

def load_audio_to_tensor(file_path, target_sr=48000):
    """Load audio as stereo PyTorch tensor with proper shape."""
    y, sr = librosa.load(file_path, sr=target_sr, mono=False)

    if y.ndim == 1:
        y = np.stack([y, y])  

    return torch.from_numpy(y).float(), sr

def save_audio(y, sr, output_path):
    """Save audio with correct shape [samples, channels]."""

    if isinstance(y, torch.Tensor):
        y = y.cpu().numpy()

    if y.shape[0] == 2:  
        y = y.T  

    sf.write(output_path, y, sr)

def enhance_audio(input_path, output_path):
    """Full processing pipeline with shape handling."""

    model = get_model(name="htdemucs")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    audio, sr = load_audio_to_tensor(input_path)
    audio = audio.to(device)
    audio = audio.unsqueeze(0)  

    with torch.no_grad():
        sources = apply_model(model, audio)  

    enhanced = sources.mean(dim=1)  
    enhanced = enhanced.squeeze(0)  

    save_audio(enhanced, sr, output_path)

if __name__ == "__main__":
    enhance_audio("input/example.mp3", "output/enhanced.wav")