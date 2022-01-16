from tkinter import *
from functools import partial
import math

window = Tk()
window.geometry("250x360")
window.title("Calculadora")

window.iconbitmap('math.ico')

def igual():
    s_numero = visor.get()
    visor.delete(0, END)
    if matematica == "soma":
        visor.insert(0, p_numero + float(s_numero))
    if matematica == "sub":
        visor.insert(0, p_numero - float(s_numero))
    if matematica == "div":
        visor.insert(0, p_numero / float(s_numero))
    if matematica == "mult":
        visor.insert(0, p_numero * float(s_numero))
    if matematica == "p":
        visor.insert(0, p_numero ** float(s_numero))

def raiz():
    primeiro_numero = visor.get()
    global p_numero
    p_numero = float(primeiro_numero)
    visor.delete(0)
    visor.insert(0, math.sqrt(p_numero))

def potencia():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "p"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def soma():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "soma"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def sub():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "sub"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def div():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "div"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def mult():
    primeiro_numero = visor.get()
    global p_numero
    global matematica
    matematica = "mult"
    p_numero = float(primeiro_numero)
    visor.delete(0,END)

def click_ponto():
    visor.insert(END, ".")

def deletar():
    visor.delete(0, END)

def click_button(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))

visor = Entry(window, width=50)
visor.pack()

botaomais = Button(window, text="C", bd=1, command=deletar)
botaomais.place(x=50, y=130, width=30)
botaomais = Button(window, text="P", bd=1, command=potencia)
botaomais.place(x=90, y=130, width=30)
botaomais = Button(window, text="/", bd=1, command=div)
botaomais.place(x=130, y=130, width=30)
botaomais = Button(window, text="√", bd=1, command=raiz)
botaomais.place(x=170, y=130, width=30)
botaomais = Button(window, text="0", bd=1, command=lambda: click_button(0))
botaomais.place(x=50, y=290, width=75)
botaomais = Button(window, text="1", bd=1, command=lambda: click_button(1))
botaomais.place(x=50, y=250, width=30)
botaomais = Button(window, text="2", bd=1, command=lambda: click_button(2))
botaomais.place(x=90, y=250, width=30)
botaomais = Button(window, text="3", bd=1, command=lambda: click_button(3))
botaomais.place(x=130, y=250, width=30)
botaomais = Button(window, text="4", bd=1, command=lambda: click_button(4))
botaomais.place(x=50, y=210, width=30)
botaomais = Button(window, text="5", bd=1, command=lambda: click_button(5))
botaomais.place(x=90, y=210, width=30)
botaomais = Button(window, text="6", bd=1, command=lambda: click_button(6))
botaomais.place(x=130, y=210, width=30)
botaomais = Button(window, text="7", bd=1, command=lambda: click_button(7))
botaomais.place(x=50, y=170, width=30)
botaomais = Button(window, text="8", bd=1, command=lambda: click_button(8))
botaomais.place(x=90, y=170, width=30)
botaomais = Button(window, text="9", bd=1, command=lambda: click_button(9))
botaomais.place(x=130, y=170, width=30)
botaomais = Button(window, text="X", bd=1, command=mult)
botaomais.place(x=170, y=170, width=30)
botaomais = Button(window, text="-", bd=1, command=sub)
botaomais.place(x=170, y=210, width=30)
botaomais = Button(window, text="+", bd=1, command=soma)
botaomais.place(x=170, y=250, width=30)
botaomais = Button(window, text="=", bd=1, command=igual)
botaomais.place(x=170, y=290, width=30)
botaomais = Button(window, text=".", bd=1, command= click_ponto)
botaomais.place(x=130, y=290, width=30)
exit_button = Button(
    window, text='Exit', bd=1,
    command=lambda:
    window.quit())
exit_button.place(x=50, y=320, width=110)

window.mainloop()