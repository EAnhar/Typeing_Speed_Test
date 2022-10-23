from Test import Test
from tkinter import * 
import tkinter as tk
from tkinter import ttk
import pymsgbox
from tkmacosx import * #for mac OS
from PIL import ImageTk
import mysql.connector
from tkinter.messagebox import showinfo

root = Tk()
root.geometry('750x500')
root.resizable(False,False)
root.title("TYPING SPEED TEST")


bg= ImageTk.PhotoImage(file="Typeing_Speed_Test-main/imgs/mainBG.jpg")
canvas= Canvas(root,width= 750, height= 500)
canvas.pack(expand=True, fill= None)
canvas.create_image(0,0,image=bg, anchor="nw")

label_0 = Label(root, text="TYPING SPEED TEST", bg='white' ,font=('Simplified Arabic Fixed', 40))
label_0.place(x=155,y=40)

label_1 = Label(root, text="employee's ID:", bg='white', font=("Simplified Arabic Fixed", 19))
label_1.place(x=65,y=165)
entry_1 = Entry(root, background='white', highlightbackground='#64A0D6')
entry_1.place(x=265,y=160, height=35, width=380)

switch_variable = StringVar(value="Level1")

# DB section
mydb = mysql.connector.connect(host='localhost', port = '1521', user='root', passwd='', db = 'pyProject')
cur = mydb.cursor()

def StartFunction():
    E_ID=entry_1.get()
    sql="select empID from dashboard where empID=%s"
    cur.execute(sql, [(E_ID)])
    result=cur.fetchall()

    if result:
        result = str(result[0]).replace(',)', '')
        result = str(result).replace('(', '')
        Test().run(str(switch_variable.get()), str(result))
        exit()
    else:
        pymsgbox.alert('ID is not found!', 'No Log')
        return False
    
def dashBoard():
    cur.execute("SELECT * FROM dashboard where score != 0 order by score desc")
    rows = cur.fetchall()

    root = tk.Tk()
    root.title('DashBoard')
    root.geometry('500x300')
    root.configure(background='white')

    #NEW
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#64A0D6", foreground="white", font=('Simplified Arabic Fixed', 18, 'bold'))

    tree = ttk.Treeview(root, columns=(1, 2), show='headings')

    # define headings
    tree.heading('1',text='employee ID')
    tree.heading('2', text='Score')
    tree.tag_configure('odd', background='light gray')
    tree.tag_configure('even', background='#FFFFFF')

    #NEW
    tree.column('1',minwidth=0,width=250, anchor=CENTER)
    #anchor make the text in the center
    tree.column('2',minwidth=0,width=250 ,anchor=CENTER)

    tag = 'odd'
    for i in rows:
        if tag == 'odd': tag = 'even'
        else: tag = 'odd'
        tree.insert('' , END, values=i, tags = (tag,))


    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            # show a message
            showinfo(title='Information', message=','.join(record))


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')



level1 = Radiobutton(root, text="Level 1", variable=switch_variable, indicatoron=False, value="Level1", 
width=20, selectcolor='#A2C9EE', bg='white', cursor='arrow',font=('Simplified Arabic Fixed',15)).place(x=60,y=265, height=35)

level2 = Radiobutton(root, text="Level 2", variable=switch_variable, indicatoron=False, value="Level2",
width=20, selectcolor='#A2C9EE', bg='white',cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=270,y=265, height=35)

level3 = Radiobutton(root, text="Level 3", variable=switch_variable, indicatoron=False, value="Level3",
width=20,selectcolor='#A2C9EE', bg='white',cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=480,y=265, height=35)


Button(root, text='Start',pady=10, width=150, activebackground='#6e9dca', activeforeground='white', command= StartFunction,
overrelief=FLAT, relief=RAISED, borderwidth=2, highlightbackground='#5a85ae', focuscolor='#5a85ae', 
overbackground='#A2C9EE', overforeground='white', cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=225,y=365)

Button(root, text='DashBoard',pady=10, width=150, activebackground='#6e9dca', activeforeground='white', command= dashBoard,
overrelief=FLAT, relief=RAISED, borderwidth=2, highlightbackground='#5a85ae', focuscolor='#5a85ae', 
overbackground='#A2C9EE', overforeground='white', cursor='arrow', font=('Simplified Arabic Fixed',15)).place(x=385,y=365)


root.mainloop()