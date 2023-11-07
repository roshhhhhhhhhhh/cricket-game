from tkinter import *
from tkinter import messagebox
import random
import csv
import game

root = Tk()
root.title('Toss')
root.geometry('935x500+200+100')
root.configure(bg='#F95151')
root.resizable(False,False)

def toss():
    global comp_option
    random_toss = random.randint(1,2)
    random_opt = random.randint(1,2)
    user_option = 0
    comp_option = 0
    if random_toss == random_opt:
        won=Label(text='you won the toss\n choose batting or bowling',fg='black',bg='white',font=('Calibri',9))
        won.place(x=380,y=100)
        user_optbat = Button(width=20,text='batting',border=0,bg='white',fg='#800000',cursor='hand2',command=batting)
        user_optbat.place(x=300,y=300)

        user_optbowl = Button(width=20,text='bowling',border=0,bg='white',fg='#800000',cursor='hand2',command=bowling)
        user_optbowl.place(x=450,y=300)

        root.destroy

    else:
        loss=Label(width=50,height=5,text='you lost the toss',fg='black',bg='white',font=('Calibri',9))
        loss.place(x=300,y=80)
        if random_opt == 1:
            comp_option = "batting"
            comp_option=Label(width=50,height=5,text='computer is batting',fg='black',bg='white',font=('Calibri',9))
            comp_option.place(x=300,y=150)

            start = Button(width=50,height=5,text='start the game',border=0,bg='white',fg='#800000',cursor='hand2',command=gaming)
            start.place(x=300,y=300)

        else:
            
            comp_option = "bowling"
            comp_option=Label(width=50,height=5,text='computer is bowling',fg='black',bg='white',font=('Calibri',9))
            comp_option.place(x=300,y=150)

            start = Button(width=50,height=5,text='start the game',border=0,bg='white',fg='#800000',cursor='hand2',command=gaming)
            start.place(x=300,y=300)
            
            root.destroy

heads = Button(width=20,text='heads',border=0,bg='white',fg='#800000',cursor='hand2',command=toss)
heads.place(x=300,y=300)

tails = Button(width=20,text='tails',border=0,bg='white',fg='#800000',cursor='hand2',command=toss)
tails.place(x=450,y=300)
def batting():
    global user_opt
    user_opt = 'batting'
    gaming()
def bowling():
     global user_opt
     user_opt = 'bowling'
     gaming()

def gaming():
    global comp_choice, runs_1, wickets_1, balls_1,comp_opt
    comp_opt = comp_option

    root = Tk()
    root.title('Game')
    root.geometry('935x500+200+100')
    root.configure(bg='#F95151')
    root.resizable(False,False)

    frame = Frame(root,width=300,height=350)
    frame.place(x=100,y=100)
    run1=Button(frame,width=20,text='1',border=0,bg='white',fg='#800000',cursor='hand2',command = onerun)
    run1.place(x=80,y=50) 
    run2=Button(frame,width=20,text='2',border=0,bg='white',fg='#800000',cursor='hand2',command = tworun)
    run2.place(x=80,y=100) 
    run3=Button(frame,width=20,text='3',border=0,bg='white',fg='#800000',cursor='hand2',command = threerun)
    run3.place(x=80,y=150) 
    run4=Button(frame,width=20,text='4',border=0,bg='white',fg='#800000',cursor='hand2',command = fourrun)
    run4.place(x=80,y=200) 
    run5=Button(frame,width=20,text='5',border=0,bg='white',fg='#800000',cursor='hand2',command = fiverun)
    run5.place(x=80,y=250) 
    run6=Button(frame,width=20,text='6',border=0,bg='white',fg='#800000',cursor='hand2',command = sixrun)
    run6.place(x=80,y=300)

    comp_choice = random.randint(1,6)


    frame = Frame(root,width=300,height=300)
    frame.place(x=500,y=100)

    score = Label(frame,text='Scoreboard',fg='#800000',bg='white',font=('Calibri',17,'bold'))
    score.place(x=90,y=5)

    runs_1 = 0
    wickets_1 = 0
    balls_1 = 0

    if balls_1 == 6:
        print("End of Over 1")

    elif balls_1 == 12:
        print("End of Over 2")

    print("Balls remaining: ",12 - balls_1)

   

def check(user_choice):
    global wickets_1, runs_1
    if user_choice == comp_choice:
        wickets_1 += 1

    elif user_opt == "batting" or comp_opt == "bowling":
       
        runs_1 += user_choice
        print(runs_1)

    elif user_opt == "bowling" or comp_opt == "batting":
       
        runs_1+=user_choice

    print("\nFinal Score:")
    print("Runs =",runs_1)
    print("wickets =",wickets_1)

def onerun():
    
    check(1)
    
   
def tworun():
    check(2)
 
def threerun():
    global user_choice
    user_choice = 3
   
def fourrun():
    global user_choice
    user_choice = 4
   
def fiverun():
    global user_choice
    user_choice = 5
    
def sixrun():
    global user_choice
    user_choice = 6
user_opt = None
bat_first =None
ball_first =None

root.mainloop()