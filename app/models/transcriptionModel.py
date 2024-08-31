from pytube import YouTube
import speech_recognition as sr
import os

class TranscriptionModel:

    @staticmethod
    def download_audio_from_youtube(youtube_url, output_path='./'):
        try:
            yt = YouTube(youtube_url)
            audio_stream = yt.streams.filter(only_audio=True).first()
            if not audio_stream:
                return None, "Nenhuma faixa de áudio encontrada para este vídeo."
            output_file = audio_stream.download(output_path)
            base, ext = os.path.splitext(output_file)
            new_file = base + '.wav'
            os.rename(output_file, new_file)
            return new_file, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def transcribe_audio(audio_file):
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_file) as source:
                audio = recognizer.record(source)
            text = recognizer.recognize_google_cloud(audio, language='pt-BR')
            return text, None
        except sr.UnknownValueError:
            return None, "Google Speech Recognition não conseguiu entender o áudio."
        except sr.RequestError as e:
            return None, f"Erro ao requisitar resultados do serviço Google Speech Recognition: {e}"
        except Exception as e:
            return None, str(e)
