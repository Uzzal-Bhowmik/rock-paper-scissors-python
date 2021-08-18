import random
import secrets
import sys
import webbrowser


# Home Page Function
def mainpage(oneortwo):
    if oneortwo == 1:
        pass
    elif oneortwo == 2:
        webbrowser.open_new_tab("https://del.dog/ghigackamo.txt")


# Startup Function
def startup():
    print("***************\n!! Rock Paper Scissors !!\n***************\n(UZZAL BHOWMIK)")
    print("\nYou can choose from\nRock(r) --- Paper(p) --- Scissors(s)    #Your Life: 5  #Your Point: 0\n                             (Prees 'e' and hit enter to exit anytime!)")



# This function is for tied result 
def if_same(youchose, random_choice, mylife, for_hope):
    if youchose == "r":
        youchose  = "ROCK"
        random_choice = "ROCK"
    if youchose == "p":
        youchose  = "PAPER"
        random_choice = "PAPER"
    if youchose == "s":
        youchose  = "SCISSORS"
        random_choice = "SCISSORS"
    print(f"\nYou: {youchose} || Computer: {random_choice}")
    print(f"\n->Result: Tied || Life: {mylife}")
    print("\n->",     for_hope)


# Main Function


def R_P_S(hchoice, hlife, count, point):
    
# Pre Declares

    list_of_hope = ["Oh,buddy! Better Luck Next Time.", "Shit!", "Slight Mistake", "Don't Lose hope!", "Try Again", 
                "No Worry, right!", "It's Ok, Mate", "Not a good choice that was!", "Sorry Buddy, Don't Worry"]


    list_of_winner = ["Well Doooone!!", "Come On", "My Man!!", "Smashed The Computer!", "That's What I'm Talking About."
                  "You're an INSPIRATION!", "Love The Game, right!"] 

    choice_list = ["r" , "p", "s"]
    
    
    for_hope = secrets.choice(list_of_hope)
    for_win = secrets.choice(list_of_winner)
    rand_choice = secrets.choice(choice_list)


# Main Things Below

    
    
# WARNING For Wrong Input
    if hchoice != "r" and hchoice != "p" and hchoice != "s" and hchoice != "e":
        print("WRONG KEY\n-> Try pressing (r)-Rock / (p)-Paper / (s)-Scissors / (e)-Exit")
        
    hchoice = hchoice.lower()

    if hchoice != rand_choice:
   
    # FOR ROCK
        if hchoice == "r" and rand_choice == "p" :

            hlife = hlife - 1
            print(f"\nYou: ROCK || Computer: PAPER")
            print()
            print(f"Result: Computer Won || Life: {hlife}")
            print("\n->",     for_hope)
            count = 0
            lost.append(1)


        if hchoice == "r" and rand_choice == "s":

            if hlife == 1:
                hlife += 1
            print(f"\nYou: ROCK || Computer: SCISSORS")
            print()
            print(f"Result: You Won || Life: {hlife}")
            print("\n->",     for_win)
            count += 1
            point = point + 100
            
            won.append(1)


     # FOR PAPER

        if hchoice == "p" and rand_choice == "s" :

            hlife = hlife - 1
            print(f"\nYou: PAPER || Computer: SCISSORS")
            print()
            print(f"Result: Computer Won || Life: {hlife}")
            print("\n->",     for_hope)
            count = 0
            lost.append(1)


        if hchoice == "p" and rand_choice == "r":

            if hlife == 1:
                hlife += 1
            print(f"\nYou: PAPER || Computer: ROCK")
            print()
            print(f"Result: You Won || Life: {hlife}")
            print("\n->",     for_win)
            count += 1
            point = point + 100
            won.append(1)


    # FOR SCISSORS

        if hchoice == "s" and rand_choice == "r" :

            hlife = hlife - 1
            print(f"\nYou: SCISSORS || Computer: ROCK")
            print()
            print(f"Result: Computer Won || Life: {hlife}")
            print("\n->",     for_hope)
            count = 0
            lost.append(1)

        if hchoice == "s" and rand_choice == "p":

            if hlife == 1:
                hlife += 1
            print(f"\nYou: SCISSORS || Computer: PAPER")
            print()
            print(f"Result: You Won || Life: {hlife}")
            print("\n->",     for_win)
            count += 1
            point = point + 100
            won.append(1)

    # If result tied
    if hchoice == rand_choice :
        if_same(hchoice, rand_choice, hlife, for_hope)
        count = 0


    # Warning for life
    if hlife == 1:
        print("You've only 1-Life left!")
        
    # Adding an exit option
    if hchoice == "e":
        print(f"\n\nYour Performance:\n     Points: {point} | Won = {len(won)} times | Lost = {len(lost)} times")
        sys.exit()


    if hlife == 0:
        print("\n\n********GAME OVER!*********")
        print(f"\nYour Performance:\n     Points: {point} | Won = {len(won)} times | Lost = {len(lost)} times")
        
    # Gift for winning 3times
    if count == 3:
        hlife += 2
        print(f"\nYou've won 3times on a row. As a gift your life is increasing by 2!!\nYour Life : {hlife}")
        

    return hlife, count, point

print("                     Home Page")
input_main = int(input("1. Start The Game\n2. Rules(Recommended if you're a first timer)\n-> "))
mainpage(input_main)
startup()
won = []
lost = []
counts = 0
points = 0
mylifes = 5
while mylifes > 0:
    
        user_input = input("Your Choice is-> ")
        
        mylifes, counts, points = R_P_S(user_input, mylifes, counts, points)
        if mylifes == 0 :
            break
            