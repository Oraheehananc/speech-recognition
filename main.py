import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="en")
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Speech not recognized")
except sr.RequestError as e:
    print(f"Error when requesting speech recognition service: {e}")
