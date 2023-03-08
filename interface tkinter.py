import tkinter as tk
#from usuario import usurario

janela = tk.Tk()
janela.title('caixa de login')

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

texto_orientação = tk.Label(janela, text='digite seu nome:',fg='white', bg='black', width=25, height=10)
texto_orientação.grid(column=0, row=0, columnspan=2, sticky='ewsn')
texto_orientação2 = tk.Label(janela, text='email',  width=5, height=5)
texto_orientação2.grid(column=0, row=2)

resposta = tk.Entry(width=40)
resposta.grid(column=0, row=1)
resposta2 = tk.Entry()
resposta2.grid(column=1, row=2)

botão = tk.Button(text='cadastrar')
botão.grid(column=1, row=3)



janela.mainloop()