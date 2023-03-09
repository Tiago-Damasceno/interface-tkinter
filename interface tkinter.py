import tkinter as tk
from tkinter import ttk
#import usuario

janela = tk.Tk()
janela.title('caixa de login')

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0,1], weight=1)

texto_orientação = tk.Label(janela, text='digite seu nome:',fg='white', bg='black', width=25, height=10)
texto_orientação.grid(column=0, row=0, columnspan=2, sticky='ewsn')
texto_orientação2 = tk.Label(janela, text='email',  width=5, height=5)
texto_orientação2.grid(column=0, row=2)

#resposta = tk.Entry(width=40)
#resposta.grid(column=0, row=1)
#resposta2 = tk.Entry()
#resposta2.grid(column=1, row=2)

nome_usuario = {
    'tiago': 1,    
    'paula': 2
   
}

email_usuario = {
    'tiago@gmail.com':1,
    'paula@gmail.com':2
}

resposta = list(nome_usuario.keys())
resposta2 = list(email_usuario.keys())

resposta = ttk.Combobox(janela, values=resposta)
resposta.grid(column=0, row=1)
resposta2 = ttk.Combobox(janela, values=resposta2)
resposta2.grid(column=1, row=2)



def usuario():
    response = resposta.get()
    response2 = resposta2.get()
    user = nome_usuario.get(response)
    user2 = email_usuario.get(response2)
    mensagem_user = tk.Label(text='nome invalido')
    mensagem_user.grid(column=0, row=3)
    mensagem_user2 = tk.Label(text='email invalido')
    mensagem_user2.grid(column=0, row=4)
    if user:
        mensagem_user['text'] = f'seu nome {response} é o user numero: {user} '
    if user2:
        mensagem_user2['text'] = f'seu email {response2} é o user numero: {user2}'


botão = tk.Button(text='cadastrar', command=usuario)
botão.grid(column=1, row=3)



janela.mainloop()