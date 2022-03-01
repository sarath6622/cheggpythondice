import random

def rollDice(sides):
    d=random.randint(1,sides)
    return d

def roll3Dice(sides):
    input("\nHit <ENTER> to roll Dice 1")
    d1=rollDice(sides)
    input("\nHit <ENTER> to roll Dice 2")
    d2=rollDice(sides)
    input("\nHit <ENTER> to roll Dice 3")
    d3=rollDice(sides)
    return d1,d2,d3

def calculate_score(d1,d2,d3):
    if d1==d2==d3:
        return d1*d2*d3
    elif d1==d2:
        return d1*d2+d3
    elif d1==d3:
        return d1*d3+d2
    elif d2==d3:
        return d2*d3+d1
    else:
        return d1+d2+d3    

def play_one_turn():
    d1,d2,d3=roll3Dice(sides)
    print("You rolled:",d1,d2,d3)
    return d1,d2,d3

def reRoll(dice,d1,d2,d3):
    d1=rollDice(sides)
    d2=rollDice(sides)
    d3=rollDice(sides)
    again = input("\nDo you like to roll again (y/n)?")
    if again=='y' or again =='yes':
        dice=int(input("WHich dice do you want to re-roll? You can choose 1,2 or 3."))

    elif dice==1:
        nD1 = rollDice(sides)
        print("You rolled:",nD1)
        score=calculate_score(nD1,d2,d3)
        print("\nTotal score:",score)

    elif dice==2:
        nD2 = rollDice(sides)
        print("You rolled:",nD2)
        score=calculate_score(d1,nD2,d3)
        print("\nTOtal score:",score)   

    elif dice==3:
        nD3 = rollDice(sides)
        print("You rolled:",nD3)
        score=calculate_score(nD1,d2,nD3)
        print("\nTOtal score:",score) 

    elif again=="n" or again=="no":
        print("\nTotal Score:",score)
    
    else:
        print("\nTotal score:",score)

def main():
    print("Welcome to TOTALITY, rolling dice game! The goal is to get the highest number possible in the three dice, \nbut dice with same value are multipilied together! Points are totaled after the final round and the winner will be declared! Enjoy!")
    rounds=int(input("\nHow many rounds you like to play?"))
    p1_wins,p2_wins=0,0
    for r in range(1,rounds+1):
        print("\nRound #{}".format(r))
        print("\nPlayer 1 its your turn")
        p1_points=play_one_turn()
        print("\nPlayer 2 its your turn")
        p2_points=play_one_turn()
        if p1_points>p2_points:
            p1_wins+=1
            print("\nRound #{} winner is player 1".format(r))

        elif p1_points<p2_points:
            p2_wins+=1
            print("\nRound #{} winner is player 2".format(r))

        else: 
            print("Its a TIE!")

    print("\nPlayer 1 won {} points".format(p1_wins))
    print("\nPlayer 2 won {} points".format(p2_wins))
    if p1_wins>p2_wins:
        print("\nPlayer 1 won the game.")
    elif p1_wins<p2_wins:
        print("\nPlayer 2 won the game.")

sides=6
main() 



