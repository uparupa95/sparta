import random
win = 0
rose = 0
draw = 0
while True:
    RSP = ["가위", "바위", "보"]
    com = random.choice(RSP)
    user = input("가위~ 바위~ 보!: ")
    print("나: " + user + "컴퓨터: " + com + "입니다.")

    if user == com:
        draw += 1
        print("비겼습니다.")
    elif (user == "가위" and com == "보") or (user == "바위" and com == "가위") or (user == "보" and com == "가위"):
        win += 1
        print("당신이 이겼습니다.")
    else:
        rose += 1
        print("당신이 졌습니다.")

    user_retry = input("재도전 하시겠습니까?")
    if user_retry.upper() == 'Y':
        continue
    else:
        print("승: " + str(win), "패: " + str(rose), "무승부: " + str(draw))
        print("게임종료")
        break
