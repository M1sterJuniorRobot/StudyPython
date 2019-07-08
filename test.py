from tkinter import *
from tkinter import messagebox

health: float = float(100)  # Здоровье монстра
damage = float(5)  # Урон героя
money = float(0)  # Монеты героя
level = float(1)  # Уровень монстра
lvl = float(1)  # Уровень увеличения дамага
a = 0
root = Tk()
Frame1 = Frame(root)

# Памятки
# Нужно сделать вывод giveinfo на экран приложения
# Желательно сделать анимацию откидывающегося монстра по середине экрана

# Функция атаки 

def attack():
    global health
    health = health - damage
    print(health)
    global money
    global level
    lbl.configure(text=str(health) + " HP")
    if health <= 5:
        money = money + 5
        print('now you have' + ' ' + str(money) + ' ' + 'money')  # not starting when health <5 ;(
    if health <= 5:
        level = level + 1
        health = level * 15 + 100


# условие при котором после убийства моба будет определяться уровень мобаА
# на каждом уровне хп монстра увеличивается на 1.75x


# покупка улучшения на 0.5

def buy1():
    global damage
    global money
    global lvl
    if money >= 10:
        money = money - 10
        damage = lvl * 0.5 + damage  # Формула расчета увеличения урона
        lvl = lvl + 1
        print('now you have ' + str(money) + ' money and ' + str(damage) + ' damage')
    else:
        print('Не достаточно средств! Побейте монстров ещё.')
        messagebox.showerror('Ошибка!', 'Не достаточно средств, побейте монстров ещё!')

# Нижнее нужно как то выводить, запихнуть в переменную скорее всего не получится...


def giveinfo():
    lbl2.configure(text="\n" +
    "Сейчас вы имеете: " + str(money) + " монет\n"
    "Ваш урон: " + str(damage) + "\n"
    "Здоровья у врага: " + str(health) + "\n"
    "Уровень монстра: " + str(level) + "\n")

# Нужно что бы giveinfo обновлялось каждый раз, когда будет происходить клик на другие кнопки. 



lbl = Label(root, text=str(health) + " HP")
lbl.grid(column=0, row=0)
lbl.place(x=148, y=90)

lbl2 = Label(root, text='')
lbl2.grid(column=1, row=1)
lbl2.place(x=90, y=50)
lbl2.pack()


but2 = Button(root, bg ="green")
but2["text"] = "BuyFirstlvl"
but2.configure(command=buy1)
but2.bind("<Button-1>")
but2.pack()
but2.place(x=150, y=600)


# Ну тут типо получить информацию о нынешнем уроне,хп,деньгах и в будущем получаемых деньгах
# Кнопка снизу для получения информации о хп, монетах, дамаге, лвл моба 

but3 = Button(root, bg ="green")
but3["text"] = "Info"
but3.configure(command=giveinfo)     
but3.bind("<Button-1>")
but3.pack()
but3.place(x=25, y=600)


# Снизу кнопка для атаки моба 

but1 = Button(root, bg ="green")
but1["text"] = "AttackThisBitch"
but1.configure(command=attack)
but1.bind("<Button-1>")
but1.pack()
but1.place(x=230, y=600)

Frame1.pack()

root.geometry("350x650")
root.mainloop()
