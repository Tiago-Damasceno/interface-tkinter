# interface-tkinter

* Interface grafica feito com Python e tkinter, para hospedagem de um pequeno CRUD feito no SQL Server, é necessario conhcimento Básico em Banco de Dados, TKinter, Figma e Proxilight designer para ultilização desse programa. Esse programa faz parte do Projeto API CRUD que estou desenvolvendo. Issues, sugestões e críticas construtivas serão muito bem vindas.

## 📋 Pré-requisitos

* PYTHON 3.11🐍

* TKINTER 🖋

* SQL SERVER 📚

## 🔧 Instalação

####TKINTER:
```from Tkinter import * / from Tkinter import ttk```
   
  * O Tkinter ja existe dentro da versão do Python então foi apenas necessario buscar algumas de suas funcionalidades, para criar uma interface grafica responsivel.

#### SQL Server:

```import pyodbc```
```dados_conexao = "Driver={SQL Server};Server=DESKTOP-L79M8K7\SQLEXPRESS;Database=bd_usuario;" /conexão = pyodbc.connect(dados_conexao)```
  * Para conexão com servidor do SQL é necessario importar a biblioteca pydbc. Criei um  bd_usuario onde seriam inseridas as informações necessárias.Também foi necessário criar um cursor que seria necessária para usar as funcionalidades do SQL.
  
###### Exemplo: ```cursor.execute(SELECT * FROM tbl_login)```

## ⚙️ Executando os testes

  * Todos os testes foram feitos no proprio console do VS Code.	

## 📦 Implantação

  * Após verificações prévias, o programa deve ser implantado no servido do Postman 

## 🛠️ Construído com

* PYTHON 3.11, TkINTER, FIGMA, PROXILIGHT DESIGNER E SQL SERVER 

## 📌 Versão

* V 0.9.0

## ✒️ Autores

 * Criado por Tiago Damasceno
  
## 📄 Licença

 * Licenciado por Tiago Damasceno (devtiago01@gmail.com)

## 🎁 Gratidão

* Quero agradecer a minha familia que esta me apoiando incondicionalmente no projeto.
* Aos meus colegas de mentoria que sempre me ajudam.
* Aos tutores que são sempre solicitos quando online
* Ao Pedro e ao Henrique meus mentores
* A Deus! sem ele nem aqui eu estaria.
