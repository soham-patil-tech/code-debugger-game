import os
import time

SCORE_FILE = "data/scores.txt"


def save_score(score):
    os.makedirs("data", exist_ok=True)
    with open(SCORE_FILE, "a") as file:
        file.write(str(score) + "\n")


def show_scores():
    if not os.path.exists(SCORE_FILE):
        print("\n📊 No previous scores found.")
        return

    print("\n📊 Previous Scores:")
    with open(SCORE_FILE, "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}. {line.strip()}")


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"⏳ Time left: {i}s", end="\r")
        time.sleep(1)
    print()
