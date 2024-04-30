import pyttsx3

# Function for converting text to speech
def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()