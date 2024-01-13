import questionary

dream_newyear = questionary.checkbox(
    "お正月に見た夢は？", choices=["富士山🗻", "タカ🦅", "茄子🍆"]
).ask()

print(f"あなたが見た夢は、{dream_newyear}ですね！最高の初夢でしたね！")
