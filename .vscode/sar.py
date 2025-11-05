import speech_recognition as sr
import pyttsx3
import sys

def listen_and_recognize():
    print(f"Hello, I'm running Python version {sys.version}")

    # Initialize the Recognizer ONCE
    recognizer = sr.Recognizer()
    
    # We will initialize the TTS engine inside the loop

    print("Say something...")
    while True:
        # 1. LISTEN TO AUDIO
        with sr.Microphone() as source:
            print("Listening...")
            
            # --- IMPORTANT ---
            # Adjust for ambient noise for better accuracy
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            # Listen for audio
            audio = recognizer.listen(source)
            
        # 2. PROCESS AND SPEAK
        try:
            # Recognize speech
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # --- THE FIX ---
            # 1. Initialize a NEW engine instance
            tts_engine = pyttsx3.init()
            tts_engine.setProperty('volume', 1.0)
            
            # 2. Say the text
            tts_engine.say(text)
            tts_engine.runAndWait()
            
            # 3. Explicitly stop and delete the engine
            tts_engine.stop()
            del tts_engine
            # --- END FIX ---
            
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            # Catch any other errors (like from a bad engine)
            print(f"An unexpected error occurred: {e}")
            # Ensure a broken engine is cleaned up
            try:
                del tts_engine
            except:
                pass


if __name__ == "__main__":
    listen_and_recognize()