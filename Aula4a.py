# 1° Passo: Importar a biblioteca sqlite3
import sqlite3

# 2° Passo: Vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# 3° Passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

# 4° Passo: Comando SQL do banco
sql = "SELECT pessoa_id, nome,nome_civil, tipo FROM pessoas"

#5° Passo: Executar o comando SQL no SQLlite (no cursor )
cursor.execute(sql)

# 6° Passo: Exibir a consulta com todos os nomes de heróis e vilões do banco de dados
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")
  