NOTES_FILE = "notes.txt"


def save_note(note):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")


def read_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            return content if content else "No notes found."
    except FileNotFoundError:
        return "You have no saved notes."
