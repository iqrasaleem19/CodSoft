

from tkinter import *
from tkinter import messagebox

def addTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    try:
        lb.delete(lb.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def updateTask():
    try:
        lb.delete(lb.curselection())
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Warning", "Please enter some task.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-Do List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
)
my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=addTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

updateTask_btn = Button(
    button_frame,
    text='Update Task',
    font=('times 14'),
    bg='#6699cc',
    padx=20,
    pady=10,
    command=updateTask
)
updateTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
