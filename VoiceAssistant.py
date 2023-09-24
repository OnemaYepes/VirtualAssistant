import io #Trabajar con archivos para guardar y manipular
from pydub import AudioSegment #Tomar el audio y volverlo un archivo temporal
import speech_recognition as sr  #Reconoce el audio
import whisper  #Motor del Asistente
import tempfile  #Generar archivos temporales
import os  #Sistema Operativo
import pyttsx3  #Generar voz
import pywhatkit

#C:\Users\jumay\Desktop\VirtualAssistant>.\venv\Scripts\activate

class VoiceAssistant:
    def __init__(self):
        pass

    def recognize_audio(self, save_path):
        audio_model = whisper.load_model('base')
        transcription = audio_model.transcribe(save_path, language='spanish', fp16=False)
        return transcription['text']

    def process_command(self, command):
        try:
            command = command.lower()
            if 'reproduce' in command:
                song_name = command.replace('reproduce', '').strip()
                print(f"Reproduciendo {song_name}")
                pywhatkit.playonyt(song_name)
        except Exception as e:
            print(e)