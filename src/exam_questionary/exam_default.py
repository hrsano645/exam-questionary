import questionary
from questionary import Choice

## 年末年始の掃除リストを作る。ゴミ出しは必須
souzi_list = [
    Choice("ゴミ出し", checked=True),
    Choice("床の掃除"),
    Choice("窓の掃除"),
    Choice("ガスコンロの掃除"),
    Choice("換気扇の掃除"),
    Choice("冷蔵庫の掃除"),
    Choice("洗濯機の掃除"),
    Choice("エアコンの掃除"),
    Choice("照明器具の掃除"),
    Choice("トイレの掃除"),
    Choice("風呂の掃除"),
]

choiced_souzi_list = questionary.checkbox(
    "掃除リストを作ります。", choices=souzi_list
).ask()

print("今年中に掃除をしたいToDoリストです！")
for heya in choiced_souzi_list:
    print(f"- [ ] {heya}")
