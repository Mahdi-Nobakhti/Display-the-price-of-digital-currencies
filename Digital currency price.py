
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox as show
from tkinter import ttk

added=[]
def get_info(coin):
        coin = coin.capitalize()
        if coin in added:
            lab.config(text="It is on the list",fg='yellow')
            lab.after(2000,clear)
            return
        added.append(coin)
        API = f"https://coinmarketcap.com/currencies/{coin}/"
        response = requests.get (API).content
        soup = BeautifulSoup(response, features="html.parser")
        symbol = soup.find('small',attrs=({'class':'nameSymbol'})).text
        API2 = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD"
        price = requests.get(API2).json()
        price = f"{price['USD']}$"
        lst = [(coin,price,symbol)]
        for contact in lst:
            tree.insert('', 0, values=contact)    
        lab.config(text="Added✅",fg='green')
        lab.after(2000,clear)
def get_info2(coin):
        coin = coin.capitalize()
        API = f"https://coinmarketcap.com/currencies/{coin}/"
        response = requests.get (API).content
        soup = BeautifulSoup(response, features="html.parser")
        symbol = soup.find('small',attrs=({'class':'nameSymbol'})).text
        API2 = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD"
        price = requests.get(API2).json()
        price = f"{price['USD']}$"
        lst = [(coin,price,symbol)]
        for contact in lst:
            tree.insert('', 0, values=contact)    

def add_currency():
    if entry_currency.get() == '' or ' ' in entry_currency.get():
        return
    try:
        get_info(entry_currency.get())
        entry_currency.delete(0,END)

    except requests.exceptions.ConnectionError:
        show.showerror('Connection Error!','Check Your Connection')
    except AttributeError:
        show.showerror('Error!','The desired currency was not found')
    except Exception:
        show.showerror('Error!','An Error occurred!try again')
def update():
    try:
        index = tree.selection()
        items = tree.item(index)
        values = items['values']
        cname = values[0]
      
        get_info2(cname)
        tree.delete(tree.selection())
        lab.config(text="Updated✅",fg='green')
        lab.after(2000,clear)

    except requests.exceptions.ConnectionError:
        show.showerror('Connection Error!','Check Your Connection')
    except IndexError:  pass
    except Exception:
        show.showerror('Error!','An Error occurred!try again')

def clear():
    lab.config(text="")
#--------------------------------
win=Tk()
win.title("Digital Currency Price")
ww = 564
wh = 230
sw = win.winfo_screenwidth()
sh = win.winfo_screenheight()
cx = sw // 2
cy = sh // 2
wl = int(cx - ww / 2)
wt = int(cy - wh / 2)-110
win.geometry(f"{ww}x{wh}+{wl}+{wt}")
win.configure(background="#1c1c1c")
win.resizable(False,False)
#--------------------------------
entry_currency = Entry(win,width=10,font='nothing 14',bg='#3f536e')
entry_currency.grid(row=0,column=0)
Button(win,text='Add Currency',command=add_currency,font='bahnschrift 13',bg='#3f536e',border=5).grid(row=1,column=0)

lab = Label(win,font="bahnschrift 12",bg='#1c1c1c')
lab.grid(row=2,column=0,rowspan=3)

Button(win,text='Update',command=update,font='bahnschrift 13',bg='#3f536e',border=5).grid(row=6,column=0,rowspan=6)

columns = ('currency', 'price', 'symbol')
tree = ttk.Treeview(win, columns=columns, show='headings')
tree.heading('currency', text='Currency Name')
tree.heading('price', text='Price')
# tree.heading('symbol', text='Symbol Name')
tree.column('currency', width=170, anchor=W)
tree.column('price', width=170, anchor=W)
tree.column('symbol', width=100, anchor=W)
tree.grid(row=0,column=1,rowspan=9,columnspan=9)
try:
    get_info('Bitcoin')
    get_info('Ethereum')
    get_info('BNB')
except :  pass
   

mainloop()