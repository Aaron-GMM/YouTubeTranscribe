from flask import Blueprint, render_template, request
from app.models.transcriptionModel import TranscriptionModel
import os

transcription_bp = Blueprint('transcription', __name__)

@transcription_bp.route('/', methods=['GET', 'POST'])
def index():
    transcription = ""
    error = ""
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        audio_file, download_error = TranscriptionModel.download_audio_from_youtube(youtube_url)
        if download_error:
            error = f"Erro ao baixar o áudio: {download_error}"
        else:
            transcription_text, transcribe_error = TranscriptionModel.transcribe_audio(audio_file)
            if transcribe_error:
                error = f"Erro na transcrição: {transcribe_error}"
            else:
                transcription = transcription_text
            # Remove o arquivo de áudio após a transcrição
            os.remove(audio_file)
    return render_template('index.html', transcription=transcription, error=error)
