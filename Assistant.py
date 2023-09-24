from AudioAssistant import AudioAssistant
from VoiceAssistant import VoiceAssistant

def main():
    audio_assistant = AudioAssistant()
    voice_assistant = VoiceAssistant()

    try:
        audio_path = audio_assistant.listen()
        if audio_path:
            response = voice_assistant.recognize_audio(audio_path)
            print(f"Texto reconocido: {response}")
            voice_assistant.process_command(response)
    except Exception as e:
        audio_assistant.talk(f"Lo lamento, no te entendí debido a este error: {e}")
        print(e)

if __name__ == '__main__':
    main()