

from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Rock, Paper, Scissors')
root.config(bg='#424242')  

Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='#757575', fg='white').pack()  

user_score = 0
computer_score = 0

def play():
    global user_score, computer_score
    choices = ['rock', 'paper', 'scissors']
    user_pick = user_take.get().lower()
    comp_pick = random.choice(choices)

    if user_pick not in choices:
        Result.set('Invalid input. Please choose rock, paper, or scissors.')
        return

    if user_pick == comp_pick:
        Result.set(f'Tie! Both selected {user_pick}.')
    elif (user_pick == 'rock' and comp_pick == 'scissors') or \
            (user_pick == 'scissors' and comp_pick == 'paper') or \
            (user_pick == 'paper' and comp_pick == 'rock'):
        Result.set(f'You win! Computer selected {comp_pick}.')
        user_score += 1
    else:
        Result.set(f'You lose! Computer selected {comp_pick}.')
        computer_score += 1

    score_label.config(text=f'User: {user_score} | Computer: {computer_score}')

def Reset():
    global user_score, computer_score
    Result.set("")
    user_take.set("")
    user_score = 0
    computer_score = 0
    score_label.config(text='User: 0 | Computer: 0')

def Exit():
    root.destroy()

user_take = StringVar()
Result = StringVar()

Label(root, text='Choose any one: rock, paper, scissors', font='arial 15 bold', bg='#424242', fg='white').place(x=20, y=70)  
Entry(root, font='arial 15', textvariable=user_take, bg='white').place(x=90, y=130)  

Entry(root, font='arial 10 bold', textvariable=Result, bg='white', width=50).place(x=25, y=250) 

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='#757575', fg='white', command=play).place(x=150, y=190) 

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='#757575', fg='white', command=Reset).place(x=70, y=310)  

Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='#757575', fg='white', command=Exit).place(x=230, y=310)  

score_label = Label(root, text='User: 0 | Computer: 0', font='arial 12 bold', bg='#424242', fg='white')
score_label.place(x=100, y=350)

root.mainloop()
