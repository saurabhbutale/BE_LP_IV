from flask import Flask, render_template, request
import librosa
import numpy as np
import wave
from pydub import AudioSegment

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audiofile' not in request.files:
        return 'No file part'

    file = request.files['audiofile']

    if file.filename == '':
        return 'No selected file'

    # Save the uploaded file
    file_path = f"./uploads/{file.filename}"
    file.save(file_path)

    # Perform the audio analysis
    forensic_result = analyze_audio(file_path)

    return render_template('index.html', result=forensic_result)

def analyze_audio(file_path):
    # Load the audio file with librosa (supports multiple formats)
    audio, sr = librosa.load(file_path)
    duration = librosa.get_duration(y=audio, sr=sr)

    # Perform basic analysis (e.g., duration, sample rate, etc.)
    forensic_data = {
        'duration': float(duration),  # Convert to float
        'sample_rate': sr,
        'n_channels': get_audio_channels(file_path),
        'metadata': get_audio_metadata(file_path),
        'mean_amplitude': float(np.mean(np.abs(audio))),  # Convert to float
        'rms_energy': float(np.mean(librosa.feature.rms(y=audio))),  # Convert to float
    }

    return forensic_data

# Helper function to get the number of channels (with support for non-WAV files)
def get_audio_channels(file_path):
    audio = AudioSegment.from_file(file_path)
    wav_file_path = file_path.rsplit('.', 1)[0] + '.wav'
    audio.export(wav_file_path, format='wav')

    with wave.open(wav_file_path, 'r') as wav_file:
        return wav_file.getnchannels()

# Helper function to extract basic metadata
def get_audio_metadata(file_path):
    audio = AudioSegment.from_file(file_path)
    metadata = {
        'channels': audio.channels,
        'frame_rate': audio.frame_rate,
        'sample_width': audio.sample_width,
        'duration_seconds': audio.duration_seconds
    }
    return metadata

if __name__ == "__main__":
    app.run(debug=True)
