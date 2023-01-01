from currency_converter import CurrencyConverter
import tkinter as tk

a=CurrencyConverter()

window = tk.Tk()
window.geometry("600x400")

def clicked():
    
        amt = int(e1.get())
        cur1= e2.get()
        cur2= e3.get()
        data= a.convert(amt,cur1,cur2)
        l5= tk.Label(window,text=data,font="Times 10 bold").place(x=250,y=300)
    

l1=tk.Label(window,text="Currency Converter",font="Times 30 bold").place(x=130,y=10)
l2= tk.Label(window,text="Enter amount Here: ",font="10").place(x=50,y=80)
e1= tk.Entry(window)
l3= tk.Label(window,text="Enter Currency: ",font="10").place(x=50,y=120)
e2= tk.Entry(window)
l4= tk.Label(window,text="Enter Currency to Convert: ",font="10").place(x=50,y=160)
e3= tk.Entry(window)
b=tk.Button(window,text="Convert",command=clicked ).place(x=250,y=250)

e1.place(x = 300, y= 88)
e2.place(x = 300, y= 128)
e3.place(x = 300, y= 169)

window.mainloop()