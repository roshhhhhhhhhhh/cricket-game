from tkinter import *
from tkinter import messagebox
import random
import csv

root = Tk()
root.title('Login')
root.geometry('935x500+200+100')
root.configure(bg='#fff')
root.resizable(False,False)
def signup():
    root.destroy()
    import loginui
def signin():
    username=user.get()
    password=int(code.get())
    with open('gameuserdetails.csv','a+',newline='') as f:
        fwriter=csv.writer(f)
        fwriter.writerow(({username,password}))
    root.destroy()



img = PhotoImage(file='login (2).png')
Label(root,image=img,bg='white').place(x=40,y=20)

frame = Frame(root,width=300,height=300)
frame.place(x=500,y=100)

heading = Label(frame,text='Sign up',fg='#800000',bg='white',font=('Calibri',23,'bold'))
heading.place(x=110,y=5)

#############__________________________________________________________________________________________

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
user.place(x=10,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=10,y=107)

#############_________________________________________________________________________________________

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Pin')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Arial',11))
code.place(x=10,y=150)
code.insert(0,'Pin')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=10,y=177)

################################################_______________________________________________________
Button(frame,width=39,pady=7,text='Sign up',bg='#800000',fg = 'white',border=2,command=signup).place(x=15,y=204)
label=Label(frame,text='already have an account?',fg='black',bg='white',font=('Calibri',9))
label.place(x=13,y=250)

sign_in = Button(frame,width=6,text='Sign in',border=0,bg='white',fg='#800000',cursor='hand2',command=signup)
sign_in.place(x=230,y=250)

root.mainloop()