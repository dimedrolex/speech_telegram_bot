import pyttsx3
import subprocess

engine = pyttsx3.init()
engine.setProperty("voice", "com.apple.speech.synthesis.voice.yuri")

def text_to_file(text):
    mp3_file = "data/test.mp3"
    out_file = "data/test_out.ogg"
    engine.save_to_file(text, mp3_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg", "-i", mp3_file, "-acodec", "libopus", out_file, "-y"])
    return out_file
    