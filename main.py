import argparse
from enhance import enhance_audio

def main():
    parser = argparse.ArgumentParser(description="AI Audio Upscaler (DSEE/UHQ Style)")
    parser.add_argument("input", help="Input audio file (MP3/WAV)")
    parser.add_argument("output", help="Output enhanced audio (WAV)")
    args = parser.parse_args()

    print(f"🔊 Upscaling {args.input}...")
    enhance_audio(args.input, args.output)
    print(f"✅ Enhanced audio saved to {args.output}")

if __name__ == "__main__":
    main()