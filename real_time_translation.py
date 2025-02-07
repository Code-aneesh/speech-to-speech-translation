import os
import speech_recognition as sr
import pyttsx3
from deep_translator import GoogleTranslator  # Free Google Translator
import mtranslate  # Backup Translator

# Initialize text-to-speech engine (Offline)
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Set speed of speech

# Free Translation using Google Translator (with Backup)
def translate(sentence, target_language="fr"):  # 'fr' for French
    try:
        # First, try Google Translate (Free API)
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(sentence)
        
        # If Google gives an error message, use backup
        if "Error" in translated_text:
            raise Exception("Google Translator Failed")

        return translated_text
    except Exception:
        # Use Backup Translator (mtranslate)
        return mtranslate.translate(sentence, target_language, "auto")

# Convert text to speech (Offline & Free)
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech recognition setup (Google Speech-to-Text API - Free)
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Speak now...")

while True:
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
            print("Listening...")
            audio = recognizer.listen(source)
        
        # Convert speech to text using Google's free API
        text = recognizer.recognize_google(audio)
        print("User:", text)

        # Translate the text
        print("Translating...")
        translated_text = translate(text, "es")  # Change 'fr' to any language code like 'es' for Spanish
        print("Translation:", translated_text)

        # Speak the translated text
        speak(translated_text)

    except sr.UnknownValueError:
        print("Could not understand audio, please try again.")
    except sr.RequestError:
        print("Speech recognition service unavailable. Check your internet connection.")
    except KeyboardInterrupt:
        print("\nExiting...")
        break
