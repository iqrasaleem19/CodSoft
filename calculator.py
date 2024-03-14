

from tkinter import *
def click(event):
    global scvalue

    if display.get() == "Error":
        scvalue.set("")
        display.update()
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(display.get())
            except Exception as e:
                value = "Error"
                print(e)
        scvalue.set(value)
        display.update()

    elif text == "C":
        scvalue.set("")
        display.update()
    elif text == "<-":
        scvalue.set(scvalue.get()[:-1])
        display.update()
    else:
        scvalue.set(scvalue.get() + text)
        display.update()

root = Tk()
root.geometry("345x640")
root.minsize(345, 640)
root.maxsize(345, 640)
root.title("Simple Calculator")
root.configure(background="black")

scvalue = StringVar()
scvalue.set("")

display = Entry(root, textvariable=scvalue, font=("times new roman", 35, "bold"),
               justify=RIGHT, bg="black", fg="white", relief=FLAT)
display.pack(side=TOP, fill=X, pady=10, padx=10, ipady=20)
buttons = [["C", "%", "<-", "/"],
           ["7", "8", "9", "*"],
           ["4", "5", "6", "-"],
           ["1", "2", "3", "+"],
           ["00", "0", ".", "="]]

for row in buttons:
    f = Frame(root, bg="black", borderwidth=0)
    f.pack(side=TOP, fill=X, padx=20)
    for btn in row:
        b = Button(f, text=btn, font=("times new roman", 28, "bold"), relief=FLAT,
                   width=3, height=1, pady=15, bg="black", fg="white",
                   activebackground="black", activeforeground="white")
        b.pack(side=LEFT)
        b.bind("<Button-1>", click)

root.mainloop()



