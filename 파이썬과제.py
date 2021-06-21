player={"이름":"김용준","경험치":2021,"레벨":20}
while True:
    sum=int(input("얻은 경험치는?: "))
    player["경험치"] += sum
    if player["경험치"] >= 2200:
        player["레벨"]+=1
        print("레벨업이에욥!! 축하드립니다!!")
        break

print("이름",player["이름"])
print("경험치",player["경험치"])
print("레벨",player["레벨"])
input()