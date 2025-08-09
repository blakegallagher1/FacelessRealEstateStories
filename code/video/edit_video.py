from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
from pathlib import Path


def assemble(visuals, audio_path, out_path="assets/output/video.mp4", fps=30):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    clips = [VideoFileClip(v).resize(height=1080) for v in visuals]
    video = concatenate_videoclips(clips, method="compose")
    narration = AudioFileClip(audio_path)
    final = video.set_audio(narration).set_duration(min(video.duration, narration.duration))
    final.write_videofile(out_path, fps=fps, codec="libx264", audio_codec="aac")
    return out_path


if __name__ == "__main__":
    # Drop some stock clips into assets/footage first
    print("Saved:", assemble(["assets/footage/clip1.mp4","assets/footage/clip2.mp4"], "assets/audio/narration.mp3"))
