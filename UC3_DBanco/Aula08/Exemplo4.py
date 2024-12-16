import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulajoao.mysql.database.azure.com",
    port=3306,
    database="aula5",  
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT nome, CPF, cpf_responsavel1, cpf_responsavel2  FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
print("Esses são alunos Cariocas:")
for nome, cpf, cpf_responsavel1, cpf_responsavel2  in resultados:
    if cpf_responsavel2 != "Null" and cpf_responsavel1 != "Null":
        print(F" O Aluno {nome} - {cpf}")
      
      

# Fechando o cursor e a conexão
cursor.close()
cnx.close()