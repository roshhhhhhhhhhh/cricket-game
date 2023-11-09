from tkinter import *
from tkinter import messagebox
import random
import csv

root = Tk()
root.title('Toss')
root.geometry('935x500+200+100')
root.configure(bg='#F95151')
root.resizable(False,False)

def toss():
    global comp_option,user_option,user_opt, root1
    random_toss = random.randint(1,2)
    random_opt = random.randint(1,2)
    user_option = 0
    comp_option = 0
    root.destroy()
    root1 = Tk()
    root1.title('Toss')
    root1.geometry('935x500+200+100')
    root1.configure(bg='#F95151')
    root1.resizable(False,False)
    if random_toss == random_opt:
        won=Label(root1,text='you won the toss\n choose batting or bowling',fg='black',bg='white',font=('Calibri',9))
        won.place(x=380,y=100)
        user_optbat = Button(root1,width=20,text='batting',border=0,bg='white',fg='#800000',cursor='hand2',command=batting)
        user_optbat.place(x=300,y=300)


        user_optbowl = Button(root1,width=20,text='bowling',border=0,bg='white',fg='#800000',cursor='hand2',command=bowling)
        user_optbowl.place(x=450,y=300)

        

    else:
        loss=Label(root1,width=50,height=5,text='you lost the toss',fg='black',bg='white',font=('Calibri',9))
        loss.place(x=300,y=80)
        if random_opt == 1:
            comp_option = "batting"
            user_opt = "bowling"
            comp_2=Label(root1,width=50,height=5,text='computer is batting',fg='black',bg='white',font=('Calibri',9))
            comp_2.place(x=300,y=150)

            start = Button(root1,width=50,height=5,text='start the game',border=0,bg='white',fg='#800000',cursor='hand2',command=gaming)
            start.place(x=300,y=300)


        else:
            
            comp_option = "bowling"
            user_opt = "batting"
            comp_1=Label(root1,width=50,height=5,text='computer is bowling',fg='black',bg='white',font=('Calibri',9))
            comp_1.place(x=300,y=150)

            start = Button(root1,width=50,height=5,text='start the game',border=0,bg='white',fg='#800000',cursor='hand2',command=gaming)
            start.place(x=300,y=300)


heads = Button(width=20,text='heads',border=0,bg='white',fg='#800000',cursor='hand2',command=toss)
heads.place(x=300,y=300)

tails = Button(width=20,text='tails',border=0,bg='white',fg='#800000',cursor='hand2',command=toss)
tails.place(x=450,y=300)

def batting():
    global user_opt,comp_option
    user_opt = 'batting'
    comp_option = 'bowling'
    gaming()
def bowling():
     global user_opt,comp_option
     user_opt = 'bowling'
     comp_option = "batting"
     gaming()

def gaming():
    global comp_choice, runs_1, wickets_1, balls_1,comp_opt,user_opt, gaura,frame
    comp_opt = comp_option
    root1.destroy()
    gaura = Tk()
    gaura.title('Game')
    gaura.geometry('935x500+200+100')
    gaura.configure(bg='#F95151')
    gaura.resizable(False,False)

    frame = Frame(gaura,width=300,height=350)
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


    frame = Frame(gaura,width=300,height=300)
    frame.place(x=500,y=100)

    score = Label(frame,text='Scoreboard',fg='#800000',bg='white',font=('Calibri',17,'bold'))
    score.place(x=90,y=5)


    runs_1 = 0
    wickets_1 = 0
    balls_1 = 0
   

def check(user_choice):
    global wickets_1, runs_1,balls_1,bat_first,ball_first,targetruns,frame

    
    if user_choice == comp_choice:
        wickets_1 += 1
        balls_1 += 1

    elif user_opt == "batting" or comp_opt == "bowling":
        bat_first ="You"
        ball_first = "Computer"
        balls_1 += 1
        runs_1 += user_choice

    elif user_opt == "bowling" or comp_opt == "batting":
        bat_first = "Computer"
        ball_first = "You"
        runs_1+=comp_choice
        balls_1 += 1
    targetruns = runs_1 + 1
    frame = Frame(gaura,width=300,height=300)
    frame.place(x=500,y=100)
    score = Label(frame,text='Scoreboard',fg='#800000',bg='white',font=('Calibri',17,'bold'))
    score.place(x=90,y=5)
    wickets = Label(frame,text=f"wickets:{wickets_1}",fg='#800000',bg='white',font=('Calibri',17,'bold'))
    wickets.place(x=90,y=100)
    runs = Label(frame,text=f"runs scored :{runs_1}",fg='#800000',bg='white',font=('Calibri',17,'bold'))
    runs.place(x=90,y=50)
    target = Label(frame,text=f"opponent needs:{targetruns}runs to win.",fg='#800000',bg='white',font=('Calibri',16,'bold'))
    target.place(x=20,y=150)
    end()

def end():  
    if balls_1 == 6:
        print("End of Over 1")

    elif balls_1 == 12:
        print("End of Over 2")
        finalscore()
    elif wickets_1 == 2:
        finalscore()
    print("Balls remaining: ",12 - balls_1)
    print("Runs =",runs_1)
    print("wickets =",wickets_1)
      
    
def finalscore():
    global wickets_1, runs_1,balls_1,bat_first,ball_first
    print("\nFinal Score:")
    print("Runs =",runs_1)
    print("wickets =",wickets_1)
    print("\n",ball_first,"needs",runs_1 + 1,"runs to win.")
    Button(frame,text='Next Innings',fg='black',font=('Calibri',13),command = secondinnings,cursor='hand2').place(x=20,y=180)
    
def onerun():
    check(1)

def tworun():
    check(2)
 
def threerun():
    check(3)
   
def fourrun():
   check(4)
   
def fiverun():
    check(5)
    
def sixrun():
    check(6)

user_opt = None


def secondinnings():
    global comp_choice, runs_2, wickets_2, balls_2,comp_opt,user_opt,gaura2
    comp_opt = comp_option
    gaura.destroy()
    gaura2 = Tk()
    gaura2.title('Game')
    gaura2.geometry('935x500+200+100')
    gaura2.configure(bg='#F95151')
    gaura2.resizable(False,False)

    frame = Frame(gaura2,width=300,height=350)
    frame.place(x=100,y=100)
    run1=Button(frame,width=20,text='1',border=0,bg='white',fg='#800000',cursor='hand2',command = one)
    run1.place(x=80,y=50) 
    run2=Button(frame,width=20,text='2',border=0,bg='white',fg='#800000',cursor='hand2',command = two)
    run2.place(x=80,y=100) 
    run3=Button(frame,width=20,text='3',border=0,bg='white',fg='#800000',cursor='hand2',command = three)
    run3.place(x=80,y=150) 
    run4=Button(frame,width=20,text='4',border=0,bg='white',fg='#800000',cursor='hand2',command = four)
    run4.place(x=80,y=200) 
    run5=Button(frame,width=20,text='5',border=0,bg='white',fg='#800000',cursor='hand2',command = five)
    run5.place(x=80,y=250) 
    run6=Button(frame,width=20,text='6',border=0,bg='white',fg='#800000',cursor='hand2',command = six)
    run6.place(x=80,y=300)

    comp_choice = random.randint(1,6)


    frame = Frame(gaura2,width=300,height=300)
    frame.place(x=500,y=100)

    score = Label(frame,text='Scoreboard',fg='#800000',bg='white',font=('Calibri',17,'bold'))
    score.place(x=90,y=5)



    runs_2 = 0
    wickets_2 = 0
    balls_2 = 0
   

def check2(user_choice):
    global wickets_2,runs_2,balls_2,bat_first,bat_second,frame

    

    if user_choice == comp_choice:
        wickets_2 += 1
        balls_2 += 1
    else:
        if bat_first == "Computer": 
            runs_2 += user_choice
            bat_second = "You"
            balls_2 +=1 

        elif bat_first == "You":
            runs_2 += comp_choice
            bat_second = "Computer"
            balls_2 +=1

        frame = Frame(gaura2,width=300,height=300)
        frame.place(x=500,y=100)
        score = Label(frame,text='Scoreboard',fg='#800000',bg='white',font=('Calibri',17,'bold'))
        score.place(x=90,y=5)
        wickets2 = Label(frame,text=f"wickets:{wickets_2}",fg='#800000',bg='white',font=('Calibri',17,'bold'))
        wickets2.place(x=90,y=100)
        runs2 = Label(frame,text=f"runs scored :{runs_2}",fg='#800000',bg='white',font=('Calibri',17,'bold'))
        runs2.place(x=90,y=50)
    
    end2()

def end2():  
    if balls_2 == 6:
        print("End of Over 1")

    elif balls_2 == 12:
        print("End of Over 2")
        finalscore2()

    elif wickets_2 == 2:
        finalscore2()

    elif runs_2 >= runs_1:
        finalscore2()
    print("Balls remaining: ",12 - balls_2)
    print("Runs =",runs_2)
    print("wickets =",wickets_2)

def finalscore2():
    global runs_2,wickets_2,balls_2
    print("\nFinal Score:")
    print("Runs =",runs_2)
    print("wickets =",wickets_2)
    result()

def one():
    check2(1)

def two():
    check2(2)
 
def three():
    check2(3)
   
def four():
   check2(4)
   
def five():
    check2(5)
    
def six():
    check2(6)

def result():
    global matchresult
    
    if runs_1 > runs_2:
        if bat_first == "You": 
            print("\nCongratulations! You won the Match by",runs_1 - runs_2,"runs.")
            matchresult = 'Player won the match by',runs_1 - runs_2, 'runs'
    
        else:
            print("\nBetter luck next time! The Computer won the Match by",runs_1 - runs_2,"runs.")
            matchresult = 'computer won the match by',runs_1 - runs_2,'runs'
    
    elif runs_2 > runs_1:
    
        if bat_second == "You": 
            print("\nCongratulations! You won the Match by",2 - wickets_2,"wickets.")
            matchresult = 'Player won the match by',2 - wickets_2,'wickets'
    
        else:
            print("\nBetter luck next time! The Computer won the Match by",2 - wickets_2,"wickets.")
            matchresult = 'computer won the match by', 2- wickets_2,'wickets'
   
    frame = Frame(gaura2,width=300,height=300)
    frame.place(x=500,y=100)
    runs = Label(frame,text=f"first innings score:{runs_1}/{wickets_1}",fg='#800000',bg='white',font=('Calibri',11,'bold'))
    runs.place(x=20,y=100)
    runs2 = Label(frame,text=f"second innings score:{runs_2}/{wickets_2}",fg='#800000',bg='white',font=('Calibri',11,'bold'))
    runs2.place(x=20,y=150)
    runs2 = Label(frame,text=f"result:{matchresult}",fg='#800000',bg='white',font=('Calibri',11,'bold'))
    runs2.place(x=20,y=200)
    save2()
    matchresult = None 
      


def save2():
    with open('cricketscore.csv','a+',newline='') as f:
        fwriter=csv.writer(f)
        fwriter.writerow(('1st Innings Score','2nd Innings Score','Match result'))
        fwriter.writerow((runs_1,runs_2,matchresult))
        f.seek(0)
        freader = csv.reader(f)
        for i in freader:
            print(i)

root.mainloop()