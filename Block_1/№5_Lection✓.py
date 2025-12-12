from tkinter import *

# Lection 9

# Tasck 1
Window1 = Tk()
Window1.title("Вікно №1")
Window1.geometry("500x600")
Window1["bg"] = "green"
Window1.mainloop()

# Tasck 2
Window2 = Tk()
Window2.title("Це вікно!")
Window2.minsize(100, 100)
Window2.geometry("400x400")
Window2["bg"] = "yellow"
Window2.mainloop()

# Tasck 3
Window3 = Tk()
Window3.title("Заголовок вікна")
Window3.geometry("1000x500")
Window3["bg"] = "white"
Window3.resizable(0,0)
Window3.mainloop()

# Tasck 4
Window4 = Tk()
Window4.title("Вікно №4")
Window4.geometry("654x456+300+400")
Window4["bg"] = "yellow"
Window4.resizable(0,0)
Window4.mainloop()

# Tasck 5
Window5 = Tk()
Window5.title("Вікно №5")
Window5.geometry("700x300+100+0")
Window5["bg"] = "blue"
Window5.resizable(0,0)
Window5.mainloop()

Window6 = Tk()
Window6.title("Вікно 5")
Window6.geometry("700x300")
Window6["bg"] = "blue"
Window6.resizable(0,0)
Window6.mainloop()