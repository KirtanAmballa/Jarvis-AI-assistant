import speech_recognition as sr
import pyttsx3


def speak(text):
    if not text:
        return

    try:
        engine = pyttsx3.init("sapi5")
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

        voices = engine.getProperty("voices")

        if voices:
            engine.setProperty("voice", voices[0].id)

        engine.say(str(text))
        engine.runAndWait()
        engine.stop()

    except Exception as e:
        print(f"TTS error: {e}")


def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, phrase_time_limit=7)

        print("Recognizing...")

        query = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print(f"You: {query}")

        return query.lower().strip()

    except sr.UnknownValueError:
        print("JARVIS: I didn't catch that.")
        return ""

    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return ""

    except OSError as e:
        print(f"Microphone error: {e}")
        return ""


def wait_for_wake_word():
    while True:
        print("Waiting for wake word...")
        query = listen()

        if "hey jarvis" in query or "jarvis" in query:
            print("Wake word detected.")
            return