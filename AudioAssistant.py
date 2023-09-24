import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import tempfile
import os
import pyttsx3


class AudioAssistant:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('rate', 145)
        self.engine.setProperty('voice', self.voices[2].id)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        try:
            with sr.Microphone() as source:
                print("Di algo...")
                self.listener.adjust_for_ambient_noise(source)
                audio = self.listener.listen(source)
                data = io.BytesIO(audio.get_wav_data())
                audio_clip = AudioSegment.from_file(data)
                save_path = self.save_audio_temporarily(audio_clip)
        except Exception as e:
            print(e)
        return save_path

    @staticmethod
    def save_audio_temporarily(audio_clip):
        temp_file = tempfile.mkdtemp()
        save_path = os.path.join(temp_file, 'temp.wav')
        audio_clip.export(save_path, format='wav')
        return save_path
    
