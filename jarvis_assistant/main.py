from modules.ai_core import ask_ai
from modules.fun import play_rps, tell_joke
from modules.info_fetcher import get_date, get_time, get_time_and_date, fetch_wikipedia
from modules.logger import log_conversation
from modules.notes import read_notes, save_note
from modules.system_control import open_calculator, open_notepad, open_recycle_bin
from modules.voice import listen, speak, wait_for_wake_word
from modules.web_control import open_google, open_music, open_youtube


def respond(user, reply):
    if not reply:
        return

    print(f"JARVIS: {reply}")

    text_to_speak = str(reply)
    speak(text_to_speak)

    log_conversation(user, reply)


def run_jarvis():
    print("Starting...")
    print(f"Hello. I am Jarvis.")
    speak("Hello. I am Jarvis.")
    print("Voice system ready.")

    while True:
        wait_for_wake_word()
        speak("Yes?")

        user = listen()
        if not user:
            continue

        if any(word in user for word in ["bye", "exit", "stop", "shutdown"]):
            respond(user, "Goodbye.")
            break

        print("Processing...")
        
        if "read notes" in user:
            respond(user, read_notes())
            continue

        if "note" in user or "remember" in user:
            speak("What should I note?")
            note = listen()

            if note:
                save_note(note)
                respond(user, "Noted.")
            else:
                respond(user, "I didn't catch the note.")
            continue

        if "open notepad" in user:
            respond(user, open_notepad())
            continue

        if "open calculator" in user:
            respond(user, open_calculator())
            continue

        if "open recycle bin" in user:
            speak("Opening Recycle Bin. Do you want me to delete everything?")
            confirmation = listen()
            respond(user, open_recycle_bin(confirmation))
            continue

        if "open youtube" in user:
            respond(user, open_youtube())
            continue

        if "open google" in user:
            respond(user, open_google())
            continue

        if "music" in user:
            respond(user, open_music())
            continue

        if "time and date" in user:
            respond(user, get_time_and_date())
            continue

        if "time" in user:
            respond(user, get_time())
            continue

        if "date" in user:
            respond(user, get_date())
            continue

        if "joke" in user or "funny" in user:
            respond(user, tell_joke(ask_ai))
            continue

        if "rock paper" in user or "play rock" in user:
            speak("Rock, paper or scissors?")
            choice = listen()
            respond(user, play_rps(choice))
            continue

        if any(phrase in user for phrase in ["who is", "what is", "tell me about"]):
            respond(user, fetch_wikipedia(user))
            continue

        respond(user, ask_ai(user))


if __name__ == "__main__":
    run_jarvis()
