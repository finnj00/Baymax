import speech_recognition as sr
import speech_to_text
import send_to_chatGPT
import text_to_speech

def main():
    messages = []
    print("Beginning conversation...")
    text_to_speech.speak_text("Hello, I am Baymax, your personal healthcare companion. How can I help you?")
    while(1):
        text = speech_to_text.record_text()
        if text == "quit" or text == "exit":
            break
        messages.append({"role": "user", "content": text}) # TODO: update for barvis (system, content)
        response = send_to_chatGPT.openAI_api_request(messages)
        text_to_speech.speak_text(response)

        # TODO: rn it crashes fast when it recieves no more user input

if __name__ == "__main__":
    main()