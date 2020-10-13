import random
print("Game Rule: Snake for s , Water for w and Gun for g.(You have only one chance!)")
print("Program Turn:\tAutomatically Selected.")
random_number = random.randint(1,3)
if random_number == 1:
    program = "s"
elif random_number == 2:
    program = "w"
elif random_number == 3:
    program = "g"

def working_of_game(program, player):
    if program == player:   #if two are equal, declare a tie!
        return None
    #check for all possiblities when program choose s
    elif program == "s":
        if player == "w":
            return False
        elif player == "g":
            return True

    # check for all possiblities when program choose w
    elif program == "w":
        if player == "g":
            return False
        elif player == "s":
            return True

    # check for all possiblities when program choose g
    elif program == "g":
        if player == "s":
            return False
        elif player == "w":
            return True
player = input("Player Turn:\t")
f = working_of_game(program, player)

print(f"Program Choose: {program}")
print(f"Player Choose: {player}")

if f == None:
    print("GAME TIE!")
elif f == True:
    print("YOU WIN THE GAME!")
else:
    print("YOU LOSE THE GAME!")

