import whisper

def transcribe_audio(audio_file):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(audio_file)

    # Return the transcript
    return result['text']
