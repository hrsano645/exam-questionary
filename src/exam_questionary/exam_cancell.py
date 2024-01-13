import sys
import questionary

your_name = questionary.text("あなたの名前を教えてください").ask()

if your_name is None:
    print("キャンセルされました")
    sys.exit(1)
