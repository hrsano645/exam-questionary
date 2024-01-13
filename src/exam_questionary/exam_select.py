import questionary

eat_newyear = questionary.select(
    "お正月に食べたものは？", choices=["おせち", "お雑煮", "カレー", "日本酒"]
).ask()

print(f"あなたが食べたり飲んだりしたのは、{eat_newyear}ですね！いいお正月でしたね！")
