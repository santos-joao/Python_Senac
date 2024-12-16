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
query = "SELECT nome, sexo, naturalidade tipo_sanguineo FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
print("Esses são alunos Cariocas:")
for nome, sexo, naturalidade in resultados:
    if sexo == "M" and naturalidade == "Rio de Janeiro":
        print(F" O Aluno {nome}")

print("Essas são alunas Paulistas:")
for nome, sexo, naturalidade in resultados:
    if sexo == "F" and naturalidade == "São Paulo":
        print(F" A Aluna {nome}")

      
      

# Fechando o cursor e a conexão
cursor.close()
cnx.close()