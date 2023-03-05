import tkinter as tk

janela = tk.Tk()
janela.title('janela de update')
janela.geometry("400x1000")

texto_orientação = tk.Label(janela, text='digite seu nome')
texto_orientação.grid(column=0, row=0, padx=10, pady=10)
botão = tk.Button(janela, text='digite seu nome')
botão.grid(column=100, row=200, padx=0, pady=150)
texto_orientação3 = tk.Label(janela, text='digite seu nome')
texto_orientação3.grid(column=10, row=10, padx=10, pady=20)

#mensagem = tk.tkinter.messagebox.showinfo(title='ola', message='oi')
#mensagem.grid(column=100, row=100)



janela.mainloop()