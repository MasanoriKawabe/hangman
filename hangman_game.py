
def hangman(word):
    wrong = 0
    stages = ["",
            "______      ",
            "|           ",
            "|     |     ",
            "|     o     ",
            "|    /|\    ",
            "|    / \    ",
            "|           "
            ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False

    print ("ハングマンにようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ちです！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!　正解は{}.".format(word))

import random
ans_list = ["desk",
            "chair",
            "applepie",
            "fishing",
            "gamble",
            "heroin",
            "idol",
            "jetplane",
            "kindergarden",
            "listerin",
            "monkey",
            "notebook",
            "people",
            "qupid",
            "round",
            "sound",
            "voice",
            "world",
            "xmen",
            "yen",
            "zebra"]
n_ans = len(ans_list) - 1 
i = random.randint(0,n_ans)
hangman(ans_list[i])
