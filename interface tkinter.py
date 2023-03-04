from tkinter import *
import tkinter

janela = Tk()
janela.title('janela de update')
janela.geometry("400x1000")

texto_orientação = Label(janela, text='digite seu nome')
texto_orientação.grid(column=0, row=0, padx=10, pady=10)
botão = Button(janela, text='digite seu nome')
botão.grid(column=100, row=200, padx=0, pady=150)
texto_orientação3 = Label(janela, text='digite seu nome')
texto_orientação3.grid(column=10, row=10, padx=10, pady=20)

mensagem = tkinter.messagebox.showinfo(title='ola', message='oi')
mensagem.grid(column=100, row=100)



janela.mainloop()