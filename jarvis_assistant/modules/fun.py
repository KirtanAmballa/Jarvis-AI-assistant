import random


def tell_joke(ask_ai):
    return ask_ai("Tell me a short, funny joke.")


def play_rps(user_move):
    options = ["rock", "paper", "scissors"]

    if user_move not in options:
        return "Invalid choice."

    computer_move = random.choice(options)

    if user_move == computer_move:
        result = "It's a tie."
    elif (user_move, computer_move) in [
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper")
    ]:
        result = "You win."
    else:
        result = "You lost."

    return f"I chose {computer_move}. {result}"
