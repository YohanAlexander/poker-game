from tkinter import *
from functools import partial

janela = Tk()
janela.title("Poker Game")
janela["background"] = "white"
janela.geometry("400x400") # Largura x Altura + Esquerda + Topo

ed = Entry(janela)
ed.place(x = 100, y = 100)

def click(botao):
    print(botao["text"])
    print(ed.get())

bt = Button(janela, width = 16, text = "Jogar")
bt.place(x = 100, y = 200)
bt["command"] = partial(click, bt)

janela.mainloop()