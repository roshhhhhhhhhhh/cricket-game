from tkinter import *
from tkinter import messagebox
import random
import csv

def start():
    print("                        WELCOME TO CRICKET GAME                    ")
    print('''

          ''')

    #introduction
    print('''                       RULES AND REGULATIONS
          1.You need to select a random number between 1 to 6.
          2.If the number selected by you and computer are same then it will be
             a Wicket,If different then the number will be added as runs for the
             player who is batting.
          3.You will get 12 Balls and 2 Wickets to play.
          4.The player or computer,who scores highest runs wins the game.''')
             



    print("\n------------------------START GAME------------------------")
     
    # Toss 
     
    print("\nHERE COMES THE TOSS")
    print("\nPress:\n1.For Heads\n2.For Tails")

    toss = int(input("Choose 1 or 2: "))

    random_toss = random.randint(1,2)
    random_opt = random.randint(1,2)
    user_opt = 0
    comp_opt = 0
    if random_toss == toss:
        print("\nYou won the toss")
        user_opt = input("Choose bat or ball: ")
    else:
        print("\nYou lost the toss")
        if random_opt == 1:
            comp_opt = "bat"
            print("Computer choose to",comp_opt)

        elif random_opt == 2:
            comp_opt = "ball"
            print("Computer choose to",comp_opt)
     
    # runs_1 is users score
    # runs_2 is computers score
    #wickets_1 is users number of wickets
    #wickets_2 is computers number of wickets

    #First Innings

    print("\n--------------------FIRST INNINGS BEGINS--------------------")
     
    runs_1 = 0
    wickets_1 = 0
    balls_1 = 0
     
    while wickets_1 != 2 and balls_1 != 12:
     
        user_choice = int(input("\nChoose any number from 1 to 6: "))
        comp_choice = random.randint(1,6)
     
        if user_choice < 1 or user_choice > 6:
            print("\nPlease choose a VALID VALUE from 1 to 6.")
     
        else:
            print("Your choice: ",user_choice,"\nComputer's choice: ",comp_choice)
     
            if user_choice == comp_choice:
                wickets_1 += 1
     
            else:
                if user_opt == "bat" or comp_opt == "ball":
                    Bat_first = "You"
                    Ball_first = "Computer"
                    runs_1 += user_choice
     
                elif user_opt == "ball" or comp_opt == "bat":
                    Bat_first = "Computer"
                    Ball_first = "You"
                    runs_1 += comp_choice
     
            print("\nScore =",runs_1,"/",wickets_1)
     
            balls_1 += 1
     
            if balls_1 == 6:
                print("End of Over 1")
     
            elif balls_1 == 12:
                print("End of Over 2")
     
            print("Balls remaining: ",12 - balls_1)
     
    print("\n--------------------End of First Innings--------------------")
    print("\n--------------------FIRST INNINGS SCORE---------------------")
     
    print("\nFinal Score:")
    print("Runs =",runs_1)
    print("wickets =",wickets_1)

    print("\n",Ball_first,"needs",runs_1 + 1,"runs to win.")
     
    # Second Innings 
     
    print("\n--------------------SECOND INNINGS BEGINS---------------------")
     
    runs_2 = 0
    wickets_2 = 0
    balls_2 = 0
     
    while wickets_2 != 2 and balls_2 != 12 and runs_2 <= runs_1:
     
        user_choice = int(input("\nChoose any number from 1 to 6: "))
        comp_choice = random.randint(1,6)
     
        if user_choice < 1 or user_choice > 6:
            print("\nPlease choose a VALID VALUE from 1 to 6.")
     
        else:
            print("Your choice: ",user_choice,"\nComputer's choice: ",comp_choice)
     
            if user_choice == comp_choice:
                wickets_2 += 1
     
            else:
                if Bat_first == "Computer": 
                    runs_2 += user_choice
                    Bat_second = "You"
     
                elif Bat_first == "You":
                    runs_2 += comp_choice
                    Bat_second = "Computer"
     
            print("\nScore =",runs_2,"/",wickets_2)
     
            balls_2 += 1
     
            if balls_2 == 6:
                print("End of Over 1")
     
            elif balls_2 == 12:
                print("End of Over 2")
     
            if runs_2 <= runs_1 and balls_2 <= 11 and wickets_2 != 2:
                print("To win:",runs_1 - runs_2 + 1,"runs needed from",12 - balls_2,"balls.")
     
    print("\n--------------------End of Second Innings--------------------")
    print("\n--------------------SECOND INNINGS SCORE---------------------")
     
    print("\nFinal Score:")
    print("Runs =",runs_2)
    print("wickets =",wickets_2)
     
    # Match Result 
     
    print("\n--------------------MATCH RESULT--------------------")

     
    if runs_1 > runs_2:
     
        if Bat_first == "You": 
            print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
            result = 'Player won the match'
     
        else:
            print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.")
            result = 'computer won the match'
     
    elif runs_2 > runs_1:
     
        if Bat_second == "You": 
            print("\nCongratulations! You won the Match by",2 - wickets_2,"wickets.")
            result = 'Player won the match'
     
        else:
            print("\nBetter luck next time! The Computer won the Match by",2 - wickets_2,"wickets.")
            result = 'computer won the match'
     
    else:
        print("The Match is a Tie ")
        result = 'match is a tie'
    print("----------------------------------------------------------------")
    print('''
             ''')
    # saving the match results in csv file named cricketscore
    with open('cricketscore.csv','a+',newline='') as f:
        fwriter=csv.writer(f)
        fwriter.writerow(('1st Innings Score','2nd Innings Score','Match result'))
        fwriter.writerow((runs_1,runs_2,result))
        f.seek(0)
        freader = csv.reader(f)
        for i in freader:
            print(i)