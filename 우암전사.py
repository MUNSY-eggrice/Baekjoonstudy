player={"청주대도서관성실반납꾼":"문영민","경험치":2021,"레벨":20}
print(player)
print("")
print("청주대도서관성실반납꾼이 책을 반납했다. 경험치를 얼마주어야 할까?")

while True:
    income = -1
    while income < 0:
        income=int(input("경험치 입력(양수):"))
        if income < 0:
            print("양수를 입력해주세요")
    player["경험치"] += income
    if player["경험치"] >= 2200:
        player["레벨"] += 1
        print("훌륭해요! 만렙입니다.")
        break
    elif player["경험치"] >= 2100:
        player["레벨"] += 1
        print("레벨업! (21레벨이 되었습니다. 만렙은 22레벨입니다.)")
        break
    elif player["경험치"] < 2100:
        print("아직 레벨업하긴 모자란 경험치 입니다.")
        print("")

while True:
    income = -1
    while income < 0:
        income=int(input("경험치 입력(양수):"))
        if income < 0:
            print("양수를 입력해주세요")
    player["경험치"] += income
    if player["경험치"] >= 2200:
        player["레벨"] += 1
        print("훌륭해요! 만렙입니다.")
        break
    elif player["경험치"] < 2200:
        print("아직 레벨업하긴 모자란 경험치 입니다.")
        print("")

print("")
print("이름",player["청주대도서관성실반납꾼"])
print("경험치",player["경험치"])
print("레벨",player["레벨"])
input()