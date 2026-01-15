import sys
import io

def check_code(user_code, expected_output):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        exec(user_code)
        output = sys.stdout.getvalue()
    except Exception as e:
        sys.stdout = old_stdout
        return False, f"❌ Error: {e}"

    sys.stdout = old_stdout
    return output == expected_output, output
