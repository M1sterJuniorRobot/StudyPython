from tkinter import *

health: float = float(100)
damage = float(5)
money = float(0)
a = 0
root = Tk()
Frame1 = Frame(root)



def attack():
    global health
    health = health - damage
    print(health)





but1 = Button(root, bg ="green")
but1["text"] = "AttackThisBitch"
but1.configure(command=attack)
but1.bind("<Button-1>")
but1.pack()


Frame1.pack()

root.geometry("500x500")
root.mainloop()