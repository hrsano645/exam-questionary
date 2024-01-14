import questionary

# questonary.confirm()でyes/noの質問をする
bougth_omikuji = questionary.confirm("おみくじを引きましたか？").ask()

# おみくじを引いた場合のみ質問する
omikuji_result = (
    questionary.select(
        "おみくじの結果はどうでしたか？",
        choices=[
            "大吉",
            "中吉",
            "小吉",
            "吉",
            "末吉",
            "凶",
            "大凶",
        ],
    )
    .skip_if(
        bougth_omikuji is False, default=False
    )  # おみくじを引いていない場合をis演算子で判定
    .ask()
)

if omikuji_result:
    print(f"おみくじの結果は{omikuji_result}でした")
else:
    print("おみくじを引いていないので結果はわかりません")
