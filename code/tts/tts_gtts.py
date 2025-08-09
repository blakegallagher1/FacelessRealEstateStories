from gtts import gTTS
from pathlib import Path


def synthesize(text, out_path="assets/audio/narration.mp3", lang="en"):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    gTTS(text=text, lang=lang, slow=False).save(out_path)
    return out_path


if __name__ == "__main__":
    sample = "This is a sample narration for Faceless Real Estate Stories."
    print("Saved:", synthesize(sample))
