import pyttsx3
import requests
import simpleaudio as sa
from pydub import AudioSegment

# Function for converting text to speech
def speak_text(command):
    engine = pyttsx3.init()
    # baymax_voice_path = "/Users/finnj00/VSCodeProjects/Python Projects/Baymax/baymax-impression.wav"
    # engine.setProperty('voice', baymax_voice_path)
    engine.say(command)
    engine.runAndWait()

def speak_text_elevenlabs(command):

    def convert_mp3_to_wav(mp3_file_path, wav_file_path):
        audio = AudioSegment.from_mp3(mp3_file_path)
        audio.export(wav_file_path, format='wav')

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "test"
    }

    data = {
    "text": command,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        # Save the audio content to a file
        with open('output.mp3', 'wb') as audio_file:
            audio_file.write(response.content)
        print('Audio content written to file "output.mp3"')

        # Play the audio using simpleaudio or any other library
        convert_mp3_to_wav("output.mp3", "output.wav")
        wave_obj = sa.WaveObject.from_wave_file("output.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
    else:
        print(f"Error: {response.status_code} - {response.text}")        