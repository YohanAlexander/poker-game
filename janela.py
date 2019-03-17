from tkinter import *
from functools import partial

janela = Tk()
janela.title("Poker Game")

table = PhotoImage(file='Baralho\mesa.png')
w = table.width()
h = table.height()

janela.geometry("%dx%d+0+0" %(w, h))

fundo = Label(janela, image=table)
fundo.place(x=0, y=0, relwidth=1, relheight=1)

#card = PhotoImage(file='Baralho\carta.png')
#carta = Label(janela, image=card)
#carta.pack(side=BOTTOM)

janela.mainloop()