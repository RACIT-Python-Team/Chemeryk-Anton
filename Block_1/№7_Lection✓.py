from tkinter import*
from tkinter import messagebox
#   Part 1

# Task 1
a=Tk()
a.title("Вікно №1")
a.geometry("500x500")
a.resizable(0,0)
d=Label(a,text="Це вікно було створено в середовищі IDLE",font="Arial 14",bg="blue",fg="white")
d.place(x=25,y=225)
a.mainloop()

# Task 2
def change (event):
    d=Label(a,text="Функція виконана",font="Calibri 14",bg="green",fg="white")
    d.place(x=225, y=225)

a=Tk()
a.title("Вікно №2")
a.geometry("500x500")
a.resizable(0,0)
a.bind("<KeyPress>",change)
a.mainloop()

# Task 3
def change(event):
    b.destroy()
    c=Label(a, text='Це вікно було створено в середовищі IDLE', font='Arial 14', bg='blue', fg='white')
    c.place(x=50, y=200)
    a['bg'] = 'blue'

a=Tk()
a.title("Вікно №3")
a.geometry("500x500")
b=Button(a,bg="blue",text="Розфарбуй",fg="black")
b.place(x=200, y=200)
a.resizable(0,0)
b.bind("<Button-3>",change)
a.mainloop()


#   Part 2

# Task 1
def change(event):
    l["text"]=e.get()

a=Tk()
a.title("Вікно №3")
a.geometry("600x700")
a["bg"]="#FF4F4F"
a.resizable(0,0)
e=Entry(a, bg="white",width="30",font="Calibri 13") 
e.place(x=180,y=350)
b=Button(a, bg="white",text="Ок",fg="black",font="Calibri 13")
b.place(x=300, y=400)
l=Label(a,text="Ви нічого не ввели.",font="Calibri 13",bg="white",fg="black")
l.place(x=250,y=300)
b.bind("<Button-1>",change)
a.mainloop()

# Task 2
def change (event):
    l["text"]=e.get()
    messagebox.showinfo("Підтвердження події","Дія виконана!")

a=Tk()
a.title("Перше вікно")
a.geometry("600x600")
a["bg"]="#FFD900"
a.resizable(0,0)
e=Entry(a, bg="white", width="30", font="Calibri 12") 
e.place(x=180,y=350)
l=Label(a, text="Ви нічого не ввели",bg="#FFFFFF",fg="#000269", font="Calibri 12")
l.place(x=250,y=300)
a.bind("<Button-3>",change)
a.mainloop()

# Task 3
def change (event):
    s=int(e.get())
    r=s*s
    messagebox.showinfo("Добуток",f"Добуток числа на нього самого: {r}")

a=Tk()
a.title("Це є вікно :)")
a.geometry("875x578")
a["bg"]="black"
a.resizable(0,0)
e=Entry(a,font="Calibri 13",width="35",bg="grey",fg="white") 
e.place(x=100,y=100)
b=Button(a,text="Ok",font="Calibri 13",bg="black",fg="white")
b.place(x=100, y=140)
l=Label(a,text="Введіть ціле число",font="Calibri 13",bg="black",fg="white")
l.place(x=100,y=50)
b.bind("<Button-3>",change)
a.mainloop()


#   Part 3

# Task 1
def newtext():
    val1=prap1.get()
    val2=prap2.get()
    val3=prap3.get()
    val4=prap4.get()
    if val1==1 and val4==1 and val2==0 and val3==0:
        label.config(text="Ви вибрали жовту гуаш")
    elif val2==1 and val3==1 and val1==0 and val4==0:
        label.config(text="Ви вибрали зелену акварель")
    elif val1==1 and val3==1 and val2==0 and val4==0:
        label.config(text="Ви вибрали жовту акварель")
    elif val2==1 and val4==1 and val1==0 and val3==0:
        label.config(text="Ви вибрали зелену гуаш")
    else:
        total=val1+val2+val3+val4
        if total>2:
            label.config(text="Вибрано занадто багато опцій. Будь ласка, виберіть лише одну пару.")
        elif total==0:
            label.config(text="Не вибрано жодної опції.")
        else:
            label.config(text="Неправильна комбінація опцій.")

Window=Tk()
Window.geometry("400x400")
label=Label(Window, text="Не вибрано")
label.place(x=100, y=50)
prap1=IntVar()
prap2=IntVar()
prap3=IntVar()
prap4=IntVar()

prapor1=Checkbutton(Window,text="Жовтий",variable=prap1,onvalue=1,offvalue=0,command=newtext)
prapor1.place(x=100, y=100)
prapor2=Checkbutton(Window,text="Зелений",variable=prap2,onvalue=1,offvalue=0,command=newtext)
prapor2.place(x=100, y=120)
prapor3=Checkbutton(Window,text="Акварель",variable=prap3,onvalue=1,offvalue=0,command=newtext)
prapor3.place(x=100, y=160)
prapor4=Checkbutton(Window,text="Гуаш",variable=prap4,onvalue=1,offvalue=0,command=newtext)
prapor4.place(x=100, y=180)
Window.mainloop()

# Task 2
def newtext(event):
    if p1.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво у маленькому ріжку")
    elif p1.get()==1 and p5.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво у середньому ріжку")
    elif p1.get()==1 and p6.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво у великому ріжку")
    elif p2.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво у маленькому ріжку")
    elif p2.get()==1 and p5.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво у середньому ріжку")
    elif p2.get()==1 and p6.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво у великому ріжку")
    elif p3.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво у маленькому ріжку")
    elif p3.get()==1 and p5.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво у середньому ріжку")
    elif p3.get()==1 and p6.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво у великому ріжку")
    else:
        messagebox.showinfo("Ваш вибір","Будь ласка, оберіть смак і розмір ріжка")

a = Tk()
a.geometry("400x400")
a.title("Магазин морозива")
l=Label(a, text="Оберіть тип морозива")
l.place(x=100,y=80)
l1 =Label(a, text="Оберіть розмір ріжку")
l1.place(x=100,y=180)
p1=IntVar()
p2=IntVar()
p3=IntVar()
p4=IntVar()
p5=IntVar()
p6=IntVar()

pr1 = Checkbutton(a,text="Ванільне",onvalue=1,offvalue=0,variable=p1)
pr1.place(x=100, y=100)
pr2 = Checkbutton(a,text="Шоколадне",onvalue=1,offvalue=0,variable=p2)
pr2.place(x=100, y=120)
pr3 = Checkbutton(a,text="Фруктове",onvalue=1,offvalue=0,variable=p3)
pr3.place(x=100, y=140)
pr4 = Checkbutton(a,text="Маленький",onvalue=1,offvalue=0,variable=p4)
pr4.place(x=100, y=200)
pr5 = Checkbutton(a,text="Середній",onvalue=1,offvalue=0,variable=p5)
pr5.place(x=100, y=220)
pr6 = Checkbutton(a,text="Великий",onvalue=1,offvalue=0,variable=p6)
pr6.place(x=100, y=240)

b = Button(a,text="Ок",font="Calibri 13",bg="white",fg="black")
b.place(x=100, y=260)
b.bind("<Button-1>",newtext)
a.mainloop()

# Task 3
def newtext(event):
    if p1.get()==1 and p3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво з шоколадной присипкой")
    elif p1.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали ванільне морозиво з кокосовою стружкою")
    elif p2.get()==1 and p3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво з шоколадной присипкой")
    elif p2.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали шоколадне морозиво з кокосовою стружкою")
    elif p5.get()==1 and p3.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво з шоколадной присипкой")
    elif p5.get()==1 and p4.get()==1:
        messagebox.showinfo("Ваш вибір","Ви вибрали фруктове морозиво з кокосовою стружкою")

a=Tk()
a.geometry("400x400")
a.title("Магазин морозива 2")
l=Label (a,text="Оберіть тип морозива")
l.place (x=100,y=80)
l1=Label (a,text="Оберіть тип присипки")
l1.place (x=100,y=180)
p1=IntVar()
p2=IntVar()
p3=IntVar()
p4=IntVar()
p5=IntVar()
p6=IntVar()

pr1=Checkbutton (a,text="Ванільне",onvalue=1,offvalue=0,variable=p1)
pr1.place (x=100,y=100)
pr2=Checkbutton (a,text="Шоколадне",onvalue=1,offvalue=0,variable=p2,)
pr2.place (x=100,y=120)
pr5=Checkbutton (a,text="Фруктове",onvalue=1,offvalue=0,variable=p5,)
pr5.place (x=100,y=140)
pr3=Checkbutton (a,text="шоколадна присипка",onvalue=1,offvalue=0,variable=p3,)
pr3.place (x=100,y=200)
pr4=Checkbutton (a,text="кокосова стружка",onvalue=1,offvalue=0,variable=p4,)
pr4.place (x=100,y=220)
b=Button(a,text="Ок",font="Calibri 13",bg="white",fg="black")
b.place(x=100,y=260)

b.bind("<Button-1>",newtext)
a.mainloop()