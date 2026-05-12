from tkinter import *
from PIL import Image, ImageTk

x = 0

lvl_c = 1

price_click = 5000

bc = False

lvl1 = 1

lvl2 = 1

lvl3 = 1

lvl4 = 1

price_newcat = 100

click_up_price = 5000

price1 = 20

price2 = 20

price3 = 20

price4 = 20

price_slot4 = 3000

slot4 = False

mis = None

money = 0

kitty_img1 = None

kitty_img2 = None

kitty_img3 = None

root = Tk()
root.geometry("1280x720")
root.title('Котики')
root.resizable(width=0, height=0)
root.configure(background='#fdd9b5')



def buy_cat():
    global x
    global kitty_img1
    x += 1
    image = Image.open('kitty.png')
    image = image.resize((50, 50))
    kitty_img1 = ImageTk.PhotoImage(image)
    label_kitty = Label(root, image=kitty_img1, bg='#fabf99')
    label_kitty.place(relx=0.6, rely=0.1, anchor=CENTER)
    btn1.place_forget()
    label_lvl1.place(relx=0.6, rely= 0.15, anchor=CENTER)
    label_price1.place(relx=0.6, rely=0.25, anchor=CENTER)
    btn_lvlup1.place(relx = 0.6, rely= 0.2, anchor =CENTER)
    btn_buy_new_cat.place(relx=0.76, rely= 0.4, anchor=CENTER)
    label_price_newcat.place(relx=0.76, rely= 0.35, anchor=CENTER)
    money_in_sec()
    get_money1()

def money_in_sec():
    global x, lvl1, lvl2, lvl3, mis, lvl4
    if x == 1:
        mis = lvl1
    elif x == 2:
        mis = lvl1+lvl2
    elif x == 3:
        mis = lvl3+lvl1+lvl2
    elif x == 4:
        mis = lvl3+lvl1+lvl2+lvl4
    label_money_in_sec.config(text=f'Монет в секунду: {mis}')




def newcat():
    global x
    global money, slot4
    if x == 1:
        if money >= price_newcat:
            x += 1
            money -= price_newcat
            buy_new_cat()
    elif x == 2:
        if money >= price_newcat:
            x += 1
            money -= price_newcat
            buy_new_cat()
    elif x == 3:
        if slot4 == True:
            if money >= price_newcat:
                x += 1
                money -= price_newcat
                buy_new_cat()



def buy_new_cat():
    global x
    global kitty_img2
    global kitty_img3
    global kitty_img4
    global price_newcat
    if x == 2:
        image = Image.open('kitty.png')
        image = image.resize((50, 50))
        kitty_img2 = ImageTk.PhotoImage(image)
        price_newcat = price_newcat * 10
        label_price_newcat.config(text= f'Цена: {price_newcat}')
        label_kitty = Label(root, image=kitty_img2, bg='#fabf99')
        label_kitty.place(relx=0.7, rely=0.1, anchor=CENTER)
        btn_lvlup2.place(relx=0.7, rely=0.2, anchor=CENTER)
        label_lvl2.place(relx=0.7, rely=0.15, anchor=CENTER)
        label_price2.place(relx=0.7, rely=0.25, anchor=CENTER)
        money_in_sec()
    if x == 3:
        image = Image.open('kitty.png')
        image = image.resize((50, 50))
        kitty_img3 = ImageTk.PhotoImage(image)
        price_newcat = price_newcat * 10
        label_price_newcat.config(text= f'Цена: {price_newcat}')
        label_kitty = Label(root, image=kitty_img3, bg='#fabf99')
        label_kitty.place(relx=0.8, rely=0.1, anchor=CENTER)
        btn_lvlup3.place(relx=0.8, rely=0.2, anchor=CENTER)
        label_lvl3.place(relx=0.8, rely=0.15, anchor=CENTER)
        label_price3.place(relx=0.8, rely=0.25, anchor=CENTER)
        money_in_sec()
        btn_new_slot4.place(relx=0.9, rely=0.2, anchor=CENTER)
        label_price_slot4.place(relx=0.9, rely=0.25, anchor=CENTER)
        prov_slot4()
    if x == 4:
        image = Image.open('kitty.png')
        image = image.resize((50, 50))
        kitty_img4 = ImageTk.PhotoImage(image)
        price_newcat = price_newcat * 10
        label_price_newcat.config(text= f'Цена: {price_newcat}')
        label_kitty = Label(root, image=kitty_img4, bg='#fabf99')
        label_kitty.place(relx=0.9, rely=0.1, anchor=CENTER)
        btn_lvlup4.place(relx=0.9, rely=0.2, anchor=CENTER)
        label_lvl4.place(relx=0.9, rely=0.15, anchor=CENTER)
        label_price4.place(relx=0.9, rely=0.25, anchor=CENTER)
        btn_buy_new_cat.place_forget()
        label_price_newcat.place_forget()
        money_in_sec()

def prov_slot4():
    global slot4, x
    if slot4 == False:
        btn_buy_new_cat.config(bg = '#dc615b')
    elif slot4 == True:
        btn_buy_new_cat.config(bg='#e19666')

def secret():
    global money
    money += 10000
    label_money.config(text=money)

root.bind('w', lambda event: secret())


def lvlup1():
    global lvl1, money
    global price1, bc
    if money >= price1:
        money -= price1
        lvl1 += 1
        price1 = int(price1 * 1.5)
        if lvl1 >= 10:
            label_info.place_forget()
            btn_autoclick_buy.config(bg = '#e19666')
            if bc == False:
                label_info_price.place(relx=0.27, rely=0.35, anchor=CENTER)

        label_lvl1.config(text=f'Уровень: {lvl1}')
        label_price1.config(text=(f'Цена: {price1}'))
        money_in_sec()

def lvlup2():
    global lvl2, money
    global price2
    if money >= price2:
        money -= price2
        lvl2 += 1
        price2 = int(price2 * 1.5)
        label_lvl2.config(text=f'Уровень: {lvl2}')
        label_price2.config(text=(f'Цена: {price2}'))
        money_in_sec()

def lvlup3():
    global lvl3, money
    global price3
    if money >= price3:
        money -= price3
        lvl3 += 1
        price3 = int(price3 * 1.5)
        label_lvl3.config(text=f'Уровень: {lvl3}')
        label_price3.config(text=(f'Цена: {price3}'))
        money_in_sec()

def add_slot4():
    global money, price_slot4, slot4
    if money >= price_slot4:
        money -= price_slot4
        slot4 = True
        btn_new_slot4.place_forget()
        label_price_slot4.place_forget()
        prov_slot4()

def lvlup4():
    global lvl4, money, price4
    global price4
    if money >= price4:
        money -= price4
        lvl4 += 1
        price4 = int(price4 * 1.5)
        label_lvl4.config(text=f'Уровень: {lvl4}')
        label_price4.config(text=(f'Цена: {price4}'))
        money_in_sec()

def buy_click():
    global lvl1, money, price_click, bc
    if lvl1 >= 10:
        if money >= price_click:
            money -= price_click
            bc = True
            btn_autoclick_buy.place_forget()
            label_info_price.place_forget()
            btn_click.place(relx=0.27, rely=0.3, anchor=CENTER)
            btn_lvlclick.place(relx=0.27, rely=0.4, anchor=CENTER)
            label_info_lvlc.place(relx=0.27, rely=0.35, anchor=CENTER)
            label_info_lvl.place(relx=0.27, rely=0.45, anchor=CENTER)
def click():
    global money, lvl_c
    money += lvl_c
    label_money.config(text=money)

def click_up():
    global money, click_up_price, lvl_c
    if money >= click_up_price:
        money -= click_up_price
        lvl_c += 1
        click_up_price = int(click_up_price * 2)
        label_info_lvlc.config(text=f'Цена прокачки клика: {click_up_price}')
        label_info_lvl.config(text = f'Уровень клика: {lvl_c}')
        prov_click()

def prov_click():
    if lvl_c >= 5:
        label_info_lvlc.place_forget()
        label_info_lvl.place(relx=0.27, rely=0.35, anchor=CENTER)
        label_info_lvl.config(text=f'Уровень клика: {lvl_c} (МАКСИМАЛЬНЫЙ)')
        btn_lvlclick.place_forget()

def get_money1():
    global lvl1, money, x, lvl2, lvl3
    if x == 4:
        money += lvl1 + lvl2 + lvl3 + lvl4
        root.after(1000, get_money1)
        label_money.config(text=money)
    if x == 3:
        money += lvl1 + lvl2 + lvl3
        root.after(1000, get_money1)
        label_money.config(text=money)
    elif x == 2:
        money += lvl1 + lvl2
        root.after(1000, get_money1)
        label_money.config(text=money)
    elif x == 1:
        money += lvl1
        root.after(1000, get_money1)
        label_money.config(text=money)



label_fon = Label(root,
                  bg = '#fabf99',
                  width = 80,
                  height = 20,
                  )
label_fon.place(relx = 0.54, rely= 0.03)

label_lvl1 = Label(root,
                   text = 'Уровень 1',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )
label_lvl3 = Label(root,
                   text = 'Уровень 1',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )
label_lvl4 = Label(root,
                   text = 'Уровень 1',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )
label_info = Label(root,
                   text='Чтоб купить эту функцию - получи 10 уровень на первом котике!',
                   fg='#aa6d46',
                   bg='#fdd9b5',
                   font=("Comic Sans MS", 10),
                   )

label_info_lvlc = Label(root,
                   text='Цена прокачки клика: 5000',
                   fg='#aa6d46',
                   bg='#fdd9b5',
                   font=("Comic Sans MS", 10),
                   )

label_info_lvl = Label(root,
                   text='Уровень клика: 1',
                   fg='#aa6d46',
                   bg='#fdd9b5',
                   font=("Comic Sans MS", 10),
                   )

label_info.place(relx=0.27, rely= 0.35, anchor=CENTER)

label_info_price = Label(root,
                   text='Цена: 5000',
                   fg='#aa6d46',
                   bg='#fdd9b5',
                   font=("Comic Sans MS", 10),
                   )

label_money = Label(root,
                    text='0',
                    fg = '#aa6d46',
                    bg = '#fdd9b5',
                    font=("Comic Sans MS", 30),
                    )
label_money.place(relx=0.27, rely=0.2, anchor=CENTER)

label_lvl2 = Label(root,
                   text='Уровень 1',
                   fg='#aa6d46',
                   bg='#fabf99',
                   font=("Comic Sans MS", 10),
                   )

label_price1 = Label(root,
                   text = 'Цена: 20',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )
label_price3 = Label(root,
                   text = 'Цена: 20',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )

label_price2 = Label(root,
                   text = 'Цена: 20',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )
label_price4 = Label(root,
                   text = 'Цена: 20',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )

label_price_slot4 = Label(root,
                   text = 'Цена: 3000',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )

label_price_newcat = Label(root,
                   text = f'Цена: {price_newcat}',
                   fg = '#aa6d46',
                   bg = '#fabf99',
                   font=("Comic Sans MS", 10),
                   )

btn1 = Button(root,
              text = 'получить первого котика',
              font=("Comic Sans MS", 20),
              bg = '#e19666',
              command= buy_cat
              )
btn1.place(relx = 0.63, rely= 0.2)

btn_lvlup1 = Button(root,
              text = 'Прокачать',
              font=("Comic Sans MS", 10),
              bg='#e19666',
              command=lvlup1
              )
btn_lvlup2 = Button(root,
              text = 'Прокачать',
              font=("Comic Sans MS", 10),
              bg='#e19666',
              command=lvlup2
              )
btn_lvlup3 = Button(root,
              text = 'Прокачать',
              font=("Comic Sans MS", 10),
              bg='#e19666',
              command=lvlup3
              )

btn_lvlup4 = Button(root,
              text = 'Прокачать',
              font=("Comic Sans MS", 10),
              bg='#e19666',
              command=lvlup4
              )

btn_buy_new_cat = Button(root,
                         text='Купить нового кота',
                         font=("Comic Sans MS", 15),
                         bg='#e19666',
                         command=newcat,
                         )

label_money_in_sec = Label(root,
                           text = 'Монет в секунду: 0',
                           font=("Comic Sans MS", 13),
                           bg='#fdd9b5',
                           fg = '#aa6d46'
                           )
label_money_in_sec.place(relx = 0.27, rely= 0.25, anchor=CENTER)

btn_new_slot4 = Button(root,
                       text='Купить слот',
                       font=("Comic Sans MS", 10),
                       bg='#e19666',
                       command=add_slot4,
                       )
btn_autoclick_buy = Button(root,
                       text='Купить возможность кликать самому',
                       font=("Comic Sans MS", 10),
                       bg='#c7c7c7',
                       command=buy_click,
                       )
btn_autoclick_buy.place(relx=0.27, rely=0.3, anchor=CENTER)
btn_click = Button(root,
                   text='Клик!',
                   font=("Comic Sans MS", 10),
                   bg='#e19666',
                   command = click
                   )
btn_lvlclick = Button(root,
                   text='Прокачать клик',
                   font=("Comic Sans MS", 10),
                   bg='#e19666',
                   command = click_up
                   )


root.mainloop()