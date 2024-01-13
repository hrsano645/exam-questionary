import questionary

your_name = questionary.text("あなたの名前を教えてください").ask()

print(f"こんにちは、{your_name}さん")
