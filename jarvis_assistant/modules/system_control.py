import os
import time
import pyautogui


def open_notepad():
    os.system("notepad")
    return "Notepad opened."


def open_calculator():
    os.system("calc")
    return "Calculator opened."


def open_recycle_bin(confirmation):
    if "delete" in confirmation or "yes" in confirmation:
        os.system("start shell:RecycleBinFolder")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("delete")
        time.sleep(1)
        pyautogui.hotkey("enter")
        return "Recycle Bin contents deleted."

    os.system("start shell:RecycleBinFolder")
    return "Okay, I won't delete anything."
