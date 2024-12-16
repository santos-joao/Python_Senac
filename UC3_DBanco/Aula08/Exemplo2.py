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
query = "SELECT nome, idade,tipo_sanguineo FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome, idade, tipo_sanguineo in resultados:
      if tipo_sanguineo == 'B+': 
        print(f"Aluno {nome} idade {idade},tem tipo sanguineo compativel ({tipo_sanguineo})")
      elif tipo_sanguineo == 'B-':
        print(f"Aluno {nome} idade {idade},tem tipo sanguineo compativel ({tipo_sanguineo})")
      elif tipo_sanguineo == 'O-':
        print(f"Aluno {nome} idade {idade},tem tipo sanguineo compativel ({tipo_sanguineo})")
      elif tipo_sanguineo == 'O+':
        print(f"Aluno {nome} idade {idade},tem tipo sanguineo compativel ({tipo_sanguineo})")
      

# Fechando o cursor e a conexão
cursor.close()
cnx.close()