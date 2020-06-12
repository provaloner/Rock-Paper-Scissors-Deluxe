import random

rating_dict = {}
rating_file = open("rating.txt", "a+") # pulls the leaderboard if you have one
for line in rating_file:
    line.split()
    rating_dict[line[0]] = line[1]
rating_file.close()

name = input("Enter your name:")

if name not in rating_dict: # sets player name
    rating_dict[name] = 0

print(f"Hello {name}")
game = input() # sets your options
if game == "": # default if you leave it blank is standard rps
    game = ["rock", "paper", "scissors"]
else:
    game = game.split(",")
print("Okay, let's start")

while True:
    choice = input()
    com_choice = random.choice(game)
    if choice == "!exit":
        print("Bye!")
        break
    elif choice == "!rating":
        print(f"Your rating: {rating_dict[name]}")
        continue
    elif choice not in game:
        print("Invalid input")
        continue

    remains = game[game.index(choice) + 1:] + game[:game.index(choice)] # decides what beats what
    loses = remains[:(len(remains) // 2)]
    wins = remains[(len(remains) // 2):]

    if choice == com_choice:
        rating_dict[name] += 50
        print(f"There is a draw ({choice})")
    elif com_choice in wins:
        rating_dict[name] += 100
        print(f"Well done. Computer chose {com_choice} and failed")
    elif com_choice in loses:
        print(f"Sorry, but computer chose {com_choice}")
