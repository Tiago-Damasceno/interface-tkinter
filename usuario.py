import pyodbc

class usurario:
    dados_conexao = "Driver={SQL Server};Server=DESKTOP-L79M8K7\SQLEXPRESS;Database=bd_usuario;"
    conexão = pyodbc.connect(dados_conexao)
    print("Conexão bem sucedida")

    cursor = conexão.cursor()


    cursor.execute('SELECT * FROM tbl_login')




    cursor.close()
    conexão.close()