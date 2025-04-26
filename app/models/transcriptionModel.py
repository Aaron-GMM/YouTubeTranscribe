# transcriptionModel.py
from pydub import AudioSegment
from pydub.utils import which
from pytubefix import YouTube
from pytubefix.cli import on_progress
import speech_recognition as sr
import os

# aponte o converter pro ffmpeg
AudioSegment.converter = which("ffmpeg") or r"C:\ffmpeg\bin\ffmpeg.exe"


class TranscriptionModel:

    @staticmethod
    def download_audio_from_youtube(youtube_url, output_path='./'):
        try:
            yt = YouTube(youtube_url, on_progress_callback=on_progress)
            audio_stream = yt.streams.get_audio_only()
            if not audio_stream:
                return None, "Nenhuma faixa de áudio encontrada."

            # baixa o .m4a
            downloaded_path = audio_stream.download(output_path=output_path)
            print(f">> downloaded_path: {downloaded_path}")

            # converte pra wav
            base, _ = os.path.splitext(downloaded_path)
            wav_path = base + '.wav'
            print(f">> wav_path: {wav_path}")

            audio = AudioSegment.from_file(downloaded_path)
            audio.export(wav_path, format='wav')

            os.remove(downloaded_path)
            return wav_path, None

        except Exception as e:
            return None, str(e)

    @staticmethod
    def transcribe_audio(audio_file):
        if not os.path.exists(audio_file):
            return None, f"Arquivo não existe: {audio_file}"

        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_file) as src:
                audio = recognizer.record(src)
            text = recognizer.recognize_google(audio, language='pt-BR')
            return text, None

        except sr.UnknownValueError:
            return None, "Não foi possível entender o áudio."
        except sr.RequestError as e:
            return None, f"Erro no serviço de Speech Recognition: {e}"
        except Exception as e:
            return None, str(e)
