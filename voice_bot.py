import speech_recognition as sr
import pyttsx3
from chatbot import get_response

engine = pyttsx3.init()

recognizer = sr.Recognizer()

while True:

    with sr.Microphone() as source:

        print("Speak your question...")

        audio = recognizer.listen(source)

        try:

            text = recognizer.recognize_google(audio)

            print("You:", text)

            response = get_response(text)

            print("Bot:", response)

            engine.say(response)
            engine.runAndWait()

        except:

            print("Sorry could not understand")