import uuid
from flask import Flask, request, render_template
from microphone_capture import record_audio
from whisper_transcriber import transcribe_audio
from database import insert_conversation, create_table

app = Flask(__name__)

# Initialize the database (ensure table is created)
create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        caller_name = request.form['caller_name']
        conversation_id = str(uuid.uuid4())

        # Capture and save the audio
        audio_file = f'{conversation_id}.wav'
        record_audio(audio_file)

        # Transcribe the audio
        transcript = transcribe_audio(audio_file)

        # Store the transcription in PostgreSQL
        insert_conversation(caller_name, conversation_id, transcript)

        return f"Transcription saved! Conversation ID: {conversation_id}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
