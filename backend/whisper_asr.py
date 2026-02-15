import whisper

# Load Whisper model only once
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Convert audio file to text using Whisper
    """
    result = model.transcribe(audio_path)
    return result["text"]
