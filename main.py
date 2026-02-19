from levels import levels
from checker import check_code
from utils import save_score, show_scores

def main():
    score = 0

    print("🐞 WELCOME TO CODE DEBUGGER GAME 🐞")
    print("Type END on a new line to submit your code.\n")

    for level_no, level in enumerate(levels, start=1):
        print(f"\n🔹 LEVEL {level_no}")
        print(level["question"])

        print("\n❌ Buggy Code:")
        print("-" * 40)
        print(level["buggy_code"])
        print("-" * 40)

        input("\nPress Enter when ready to fix the code...")

        print("\n✏️ Enter your corrected code below:")
        user_lines = []

        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            user_lines.append(line)

        user_code = "\n".join(user_lines)

        is_correct, result = check_code(user_code, level["expected_output"])

        if is_correct:
            print("✅ Correct! Level passed.")
            score += 10
        else:
            print("❌ Incorrect solution.")
            print("\n🔎 Your Output:")
            print(result)

    print("\n🎉 GAME OVER")
    print(f"🏆 Final Score: {score}")

    save_score(score)
    show_scores()

if __name__ == "__main__":
    main()
