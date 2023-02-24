from tkinter import *

def click(event):
    global ipscreen
    text=event.widget.cget("text")
    print(text)

    if text=="=":
        if ipscreen.get().isdigit():
            value=int(ipscreen.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
                

        ipscreen.set(value)
        screen.update()
        
    elif text=="AC":
        ipscreen.set("")
        screen.update()

    else:
        ipscreen.set(ipscreen.get()+text)
        screen.update()
    
root =Tk()
root.geometry("400x550")
root.configure(bg='black')

ipscreen=StringVar()
ipscreen.set("")

screen=Entry(root,textvar=ipscreen,font='times 25 bold',bg='black',fg='white',bd=0)
screen.pack(fill=X,ipadx=20,pady=20,padx=20)

f=Frame(root,bg="black")
b=Button(f,text="AC",padx=28,pady=22,font='times 10 bold',bd=0,bg='#C0C0C0')
b.pack(side=LEFT ,padx=10,pady=10,ipadx=39)
b.bind("<Button-1>",click)


b=Button(f,text="%",padx=28,pady=22,font='times 10 bold',bd=0,bg='#C0C0C0')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=28,pady=22,font='times 10 bold',bd=0,bg='#FFA500')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text="9",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT ,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="7",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="*",padx=28,pady=22,font='times 10 bold',bd=0,bg='#FFA500')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text="6",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT ,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="4",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=28,pady=22,font='times 10 bold',bd=0,bg='#FFA500')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text="3",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT ,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="1",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="+",padx=28,pady=22,font='times 10 bold',bd=0,bg='#FFA500')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root,bg="black")
b=Button(f,text="0",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT ,padx=10,pady=10,ipadx=50)
b.bind("<Button-1>",click)

b=Button(f,text=".",padx=28,pady=22,font='times 12 bold',bd=0,bg='#808080',fg='white')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

b=Button(f,text="=",padx=28,pady=22,font='times 10 bold',bd=0,bg='#FFA500')
b.pack(side=LEFT,padx=10,pady=10)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
