import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-GONE;"
    "Database=DB_COMPUGRAF;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

Nome = 'Ana'
Sobrenome = 'Silva'
Cep = '01001000'
Rua = 'Rua A'
Cidade = 'São Paulo'
UF = 'SP'
Bairro = 'Centro'
Numero = '123'
Complemento = 'Apto 101'
Profissao = 'Engenheira'
PessoaID = 1

cursor = conexao.cursor()

comandoCreate = """
INSERT INTO Pessoas (Nome, Sobrenome, Cep, Rua, Cidade, UF, Bairro, Numero, Complemento, Profissao)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""
dadosCreate = (Nome, Sobrenome, Cep, Rua, Cidade, UF, Bairro, Numero, Complemento, Profissao)

comandoDelet = "DELETE FROM Pessoas WHERE PessoaID = ?"

comandoRead = "SELECT * FROM Pessoas"

comandoUpdate = """
UPDATE Pessoas
SET Nome = ?, Sobrenome = ?, Cep = ?, Rua = ?, Cidade = ?, UF = ?, Bairro = ?, Numero = ?, Complemento = ?, Profissao = ?
WHERE PessoaID = ?
"""
dadosUpdate = (Nome, Sobrenome, Cep, Rua, Cidade, UF, Bairro, Numero, Complemento, Profissao, PessoaID)

cursor.execute(comandoCreate, dadosCreate)
conexao.commit()

cursor.execute(comandoDelet, (PessoaID,))
conexao.commit()

cursor.execute(comandoRead)
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)

cursor.close()
conexao.close()
