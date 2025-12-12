from tkinter import *
from tkinter import messagebox
#       Lection 10

#   Part 1

# Task 1
def change(event):
    a.geometry("400x300")
    a["bg"]="green"
    a.title("Рівне")
    but.destroy()


a=Tk()
a.title("Місто")
but=Button(a,bg="green",fg="red",font="Times 12",text="Press left mouse button")
but.place(x=25,y=100)
a.bind("<Button-1>", change)
a.mainloop()


# Task 2
def change(event):
    a.geometry("700x600")
    a["bg"]="violet"
    a.title("РФКІТ")
    a.resizable(0,0)

a=Tk()
a.title("Коледж")
a.bind("<Button-3>", change)
a.mainloop()

# Task 3
def change(event):
    a.geometry("300x200")
    a["bg"]="yellow"
    a.title("Чемерик Антон")
    a.minsize(200,100)
    a.maxsize(1000,900)

a=Tk()
a.title("Ім'я")
a.bind("<KeyPress>", change)
a.mainloop()


# Task 4
def change(event):
    a.geometry("500x600")
    a["bg"]="gray"
    a.title("ІПЗ-2/2")
    a.minsize(400,500)
    a.maxsize(900,1000)
a=Tk()
a.title("Група")
def info(event):
   messagebox.showinfo("Клас","Я навчаюся у 8 класі!")

a.bind("<KeyPress>", change)
a.bind("<Button-1>", info)
a.mainloop()


# Task 5
def change(event):
    a.geometry("400x300")
    a["bg"]="green"
    a.title("Вікно №2")
    a.minsize(400,500)
    a.maxsize(900,1000)

a=Tk()
a.title("Вікно №1")
a.geometry("700x400")
a["bg"]="red"
a.bind("<Button-1>", change)
a.mainloop()


#   Part 2

# Task 1
def change(event):
    a.geometry("650x560")
    a["bg"]="green"
    a.title("Вікно №2")
    but=Button(a,text="Розфарбуй",bg="blue",fg="black")
    
a=Tk()
but=Button(a,text="Розфарбуй",bg="yellow",fg="black")
but.place(x=100, y=90)
a.title("Вікно №1")
a.geometry("400x300")
a["bg"]="red"
but.bind("<Button-1>",change)
a.mainloop()

# Task 2
def change(event):
    a.geometry("560x435")
    but.place(x=240, y=217)
    a["bg"]="yellow"
    a.title("Завдання виконано!")
    messagebox.showinfo("Виконано","Зміни застосовані!")
    
a=Tk()
but=Button(a, bg="pink", text="Змінити", fg="blue")
but.place(x=225, y=225)
a.title("Це вікно Python")
a.geometry("500x500")
a["bg"]="red"
but.bind("<Button-3>",change)
a.mainloop()

# Task 3
def change(event):
    a.geometry("560x435")
    but.place(x=240, y=217)
    a["bg"]="yellow"
    a.title("Завдання виконано!")
    messagebox.showinfo("Виконано","Зміни застосовані!")
    
a=Tk()
but=Button(a, bg="pink", text="Змінити", fg="blue")
but.place(x=225, y=225)
a.title("Це вікно Python")
a.geometry("500x500")
a["bg"]="red"
but.bind("<Button-3>",change)
a.mainloop()