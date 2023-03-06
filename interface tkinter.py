import tkinter as tk

janela = tk.Tk()
janela.title('caixa de login')

texto_orientação = tk.Label(janela, text='digite seu nome:',fg='white', bg='black', width=15, height=5)
texto_orientação.grid(column=0, row=0)
texto_orientação2 = tk.Label(janela, text='email',  width=15, height=5)
texto_orientação.grid(column=1, row=3)

resposta = tk.Entry()
resposta.grid(column=0, row=1)
resposta2 = tk.Entry()
resposta2.grid(column=0, row=4)




janela.mainloop()