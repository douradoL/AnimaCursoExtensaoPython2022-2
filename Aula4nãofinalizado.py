  # 1° Passo: Importar a biblioteca sqlite3
import sqlite3

# 2° Passo: Vamos estabelecer uma conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

# 3° Passo: Criar um objeto do tipo cursor
cursor = conexao.cursor()

# 4° Passo: Comando para inserir herói ou vilão
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

# 5° Passo: Executar o comando SQL
print(cursor.execute(sql))

# 6° Passo: Confirmar o INSERT com commit() e fechar o banco
cursor.commit()
conexao.close()
