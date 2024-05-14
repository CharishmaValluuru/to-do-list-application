
import tkinter
from tkinter import*
def add():
     task=entry.get()
     if task:
         listbox.insert(END,task)
entry.delete(0,END)
def remove():
     try:
         result=listbox.curselection()[0]
         listbox.delete(result)
     except IndexError:
         pass
def mark():
     try:
         result=listbox.curselection()[0]
         listbox.itemconfig(result,bg="#sky blue")
     except IndexError:
         pass
     
     root=Tk()
 
root.title("TO-DO-LIST-APP")
root.geometry("410x650+400+100")
root.resizable(False,False) 
 
 
icon=PhotoImage(file="C:\\Users\\charishma valluru\\Downloads\\notebook.png")
root.iconphoto('Flase',icon)
 
 
photo=PhotoImage(file="C:\\Users\\charishma valluru\\Downloads\\todo.png")
Label(root,text="ADD LIST",image=photo).pack()


text=Label(root,text="ADD LIST",font=("Arial",25,"bold"),bg="#606060",relief=SUNKEN)
text.place(x=120,y=30)

entry=Entry(root,font=("arial",15),width=28,bd=5,bg="#93ff75",relief=SUNKEN)
entry.place(x=0,y=115)

button=Button(text="ADD",font=("arial",10,"bold"),command=add,width=10,bd=6,bg="#de9bce")
button.place(x=320,y=115)


frame1=Frame(root,bd=3,width=700,height=280,bg="#fff875")
frame1.pack(pady=(95,0))

listbox=Listbox(frame1,font=('arial',12),width=40,height=16,bg='white')
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


button1=Button(text="Clear The File",bg="#6970c2",command=remove,bd=5,relief=SUNKEN,width=27,font=("arial",12,"bold"))
button1.place(x=60,y=530)

button1=Button(text="Mark As Read",bg="sky blue",command=mark,bd=5,relief=RAISED,width=27,font=("arial",12,"bold"))
button1.place(x=60,y=580)



