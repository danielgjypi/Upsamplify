# 🔊 Upsamplify
*Upscale compressed audio like Sony DSEE or Samsung UHQ using AI*  

## 🚀 Features  
- **AI-Powered Upscaling** - Restores lost high frequencies (MP3 → Lossless-like)  
- **Cross-Platform** - Works on Windows/macOS/Linux  
- **Two Interfaces**  
  - **CLI** for power users.
  - **Streamlit GUI** because it's prettier.  

# ⚙️ Installation  

### Prerequisites  
- Python 3.8+  
- FFmpeg (for MP3 support)  

### Install FFmpeg: 

#### Linux (Debian/Ubuntu)
```bash
sudo apt install ffmpeg
```

#### macOS (Homebrew)
```bash
brew install ffmpeg
```

#### Windows (Chocolatey)
```bash
choco install ffmpeg
```

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/audio_upscaler.git
cd audio_upscaler
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Download AI Models (Auto-download on first run)
```bash
python -c "from demucs.pretrained import get_model; get_model(name='htdemucs')"
```

# 🖥️ Usage
### CLI Version
```bash
# Single file
python main.py input.mp3 output.wav
```

### Web GUI
```bash
streamlit run app.py
```
Opens `http://localhost:8501` in your browser.

# 🛠️ Troubleshooting
### 1. Streamlit Not Found
**Fix:** Add Python scripts folder to PATH

#### Linux/macOS
```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc && source ~/.bashrc
```
#### Windows: Add this to PATH manually:
```
 C:Users\<YOU>\AppData\Roaming\Python\Python3XX\Scripts
```

### 2. CUDA Out of Memory
Edit `enhance.py`:
```python
device = torch.device("cpu")  # Change from "cuda"
```

### 3. "Invalid Shape" Errors
- Convert stereo files to mono first using Audacity/FFmpeg
- Trim files to <10 minutes if processing fails

# 📂 Project Structure
```
audio_upscaler/
├── input/                  # Default input folder
│   └── sample.mp3          # Example file
├── output/                 # Enhanced audio saved here
├── src/
│   ├── enhance.py          # Core AI processing
│   ├── main.py             # CLI interface
│   └── app.py              # Streamlit GUI
├── requirements.txt        # Dependencies
└── README.md               # This file
```

# ❓ FAQ
### Q: How much quality improvement can I expect?
> A: Typical results:
- MP3 128kbps → Sounds like ~256kbps
- MP3 320kbps → Near-CD quality

### Q: Why is the output file so large?
> A: WAV is uncompressed. Use ffmpeg to convert to FLAC for smaller files:
```bash
ffmpeg -i output.wav -compression_level 12 output.flac
```

### Q: Can I use this commercially?
> A: Yes! MIT License allows any use (credit appreciated but not required).
