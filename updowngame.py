import random
random_number = random.randint(1, 100)
game = 0
while True:
    user = int(input("1~100 중 입력하세요: "))
    game += 1
    if (random_number < user):
        print("down")
    elif (random_number > user):
        print("up")
    elif (random_number == user):
        print("정답입니다. 시도한 횟수는" + str(game) + "번 입니다.")
        break

