from random import randint

title = "rock-paper-scissor Game"
print(title)
print(f"{'=' * len(title)}")

weapon = ("rock", "paper", "scissor")

player = input("Choose your weapon(rock| paper| scissor): ")
computer = weapon [randint(0,2)]

if player == computer:
    print("player uses", player)
    print("computer uses", computer)
    print("nobody wins!")
elif player == "rock":
    if computer == "paper":
        print("player uses", player)
        print("computer uses", computer)
        print("nobody wins!")
    elif computer == "scissor":
        print("player uses", player)
        print("computer uses", computer)
        print("player wins!")
elif player == "paper":
    if computer == "rock":
        print("player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == "scissor":
        print("player uses", player)
        print("computer uses", computer)
        print("computer wins!")
elif player == "scissor":
    if computer == "rock":
        print("player uses", player)
        print("computer uses", computer)
        print("computer wins!")
    elif computer == "scissor":
        print("player uses", player)
        print("computer uses", computer)
        print("player wins!")

else:
    print("wrong weapon!")