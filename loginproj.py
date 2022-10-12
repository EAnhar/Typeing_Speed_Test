from finalCode import Test
from curses import color_content
from tkinter import* 
from tkmacosx import *
from PIL import ImageTk

root = Tk()
root.geometry('750x500')
root.resizable(False,False)
root.title("TYPING SPEED TEST")

bg= ImageTk.PhotoImage(file="imgs/startBG.jpg")
canvas= Canvas(root,width= 400, height= 200)
canvas.pack(expand=True, fill= BOTH)
canvas.create_image(0,0,image=bg, anchor="nw")

label_0 = Label(root, text="TYPING SPEED TEST", bg='white' ,font=('Simplified Arabic Fixed', 40))
label_0.place(x=155,y=40)

label_1 = Label(root, text="Player's Name:", bg='white', font=("Simplified Arabic Fixed", 19))
label_1.place(x=65,y=165)
entry_1 = Entry(root, bg='white', highlightbackground='#6e9dca')
entry_1.place(x=265,y=160, height=35, width=380)


def StartFunction():
    Test().run(str(switch_variable.get()))
    exit()
    
switch_variable = StringVar(value="Level1")

level1 = Radiobutton(root, text="Level 1", variable=switch_variable, indicatoron=False, value="Level1", 
width=20, selectcolor='#A2C9EE', bg='white', cursor='arrow',font=('Simplified Arabic Fixed',15)).place(x=60,y=265, height=35)

level2 = Radiobutton(root, text="Level 2", variable=switch_variable, indicatoron=False, value="Level2",
width=20, selectcolor='#A2C9EE', bg='white',cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=270,y=265, height=35)

level3 = Radiobutton(root, text="Level 3", variable=switch_variable, indicatoron=False, value="Level3",
width=20,selectcolor='#A2C9EE', bg='white',cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=480,y=265, height=35)


Button(root, text='Start',pady=10, width=200, activebackground='#6e9dca', activeforeground='white', command= StartFunction,
overrelief=FLAT, relief=RAISED, borderwidth=2, highlightbackground='#5a85ae', focuscolor='#5a85ae', 
overbackground='#A2C9EE', overforeground='white', cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=265,y=365)


root.mainloop()