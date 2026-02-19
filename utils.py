import os

SCORE_FILE = "data/scores.txt"


def save_score(score: int) -> None:
    """Save the player's score to a file."""
    os.makedirs("data", exist_ok=True)
    with open(SCORE_FILE, "a", encoding="utf-8") as file:
        file.write(f"{score}\n")


def show_scores() -> None:
    """Display all previous scores."""
    if not os.path.exists(SCORE_FILE):
        print("\n📊 No previous scores found.")
        return

    print("\n📊 Previous Scores:")
    with open(SCORE_FILE, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            print(f"{i}. {line.strip()}")
